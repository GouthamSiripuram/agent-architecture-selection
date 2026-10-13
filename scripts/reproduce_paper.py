"""Reproduce illustrative utility calculations; no empirical outcomes are used."""
from pathlib import Path
import sys, json, hashlib
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from agent_arch_select.model import COEFFICIENTS, ARCHITECTURES, score_architectures, recommend_architecture

def main():
    for sub in ['results','paper/tables','paper/figures']:
        (ROOT/sub).mkdir(parents=True,exist_ok=True)
    source=ROOT/'data/architecture_scenarios_v0_2.jsonl'
    rows=[json.loads(x) for x in source.read_text().splitlines()]
    assert len(rows)==48 and all(r['synthetic'] is True for r in rows)
    labels=dict(zip(ARCHITECTURES,['SA','SAT','PEV','HMA']))
    lambdas=[0,.5,1,2,4]
    records=[]
    for lam in lambdas:
        for row in rows:
            scores=score_architectures(row,lam)
            records.append(dict(scenario_id=row['scenario_id'],cost_aversion=lam,
                                recommended=recommend_architecture(row,lam),**scores))
    frame=pd.DataFrame(records)
    frame.to_csv(ROOT/'results/synthetic_utilities.csv',index=False)
    counts=pd.crosstab(frame.recommended,frame.cost_aversion).reindex(index=ARCHITECTURES,columns=lambdas,fill_value=0)
    assert all(counts.sum()==48)
    counts.to_csv(ROOT/'results/synthetic_selection_counts.csv')
    table=[r'\begin{tabular}{lrrrrr}',r'\toprule',r'Architecture & $\lambda=0$ & $0.5$ & $1$ & $2$ & $4$ \\',r'\midrule']
    for key in ARCHITECTURES: table.append(labels[key]+' & '+' & '.join(str(int(x)) for x in counts.loc[key])+r' \\')
    table += [r'\bottomrule',r'\end{tabular}']
    (ROOT/'paper/tables/summary.tex').write_text('\n'.join(table)+'\n')
    table=[r'\begin{tabular}{lrrrrrr}',r'\toprule',r'Architecture & $\alpha$ & $\beta$ & $\gamma$ & $\delta$ & $\eta$ & $\zeta$ \\',r'\midrule']
    for key in ARCHITECTURES: table.append(labels[key]+' & '+' & '.join(f'{COEFFICIENTS[key][c]:.2f}' for c in ['D','S','V','H','P','K'])+r' \\')
    table += [r'\bottomrule',r'\end{tabular}']
    (ROOT/'paper/tables/coefficients.tex').write_text('\n'.join(table)+'\n')
    fig,ax=plt.subplots(figsize=(6.2,3.1),layout='constrained')
    for a,marker in zip(ARCHITECTURES,['o','s','^','D']):
        ax.plot(lambdas,counts.loc[a],marker=marker,label=labels[a])
    ax.set(xlabel='Resource aversion (lambda)',ylabel='Synthetic selection count',ylim=(0,48),xticks=lambdas)
    ax.grid(alpha=.2); ax.legend(frameon=False,ncol=4,fontsize=9,loc='upper center')
    fig.savefig(ROOT/'paper/figures/sensitivity.pdf',metadata={'CreationDate':None,'ModDate':None}); plt.close(fig)
    (ROOT/'results/input_hashes.json').write_text(json.dumps({source.name:hashlib.sha256(source.read_bytes()).hexdigest()},indent=2)+'\n')
    print(counts.to_string())

if __name__=='__main__': main()
