import os, json, urllib.request, html
from pathlib import Path
USER='Sahilpreetsinghvirdi'; TOKEN=os.environ['GITHUB_TOKEN']; OUT=Path('assets'); OUT.mkdir(exist_ok=True)
def api(url,payload=None):
    req=urllib.request.Request(url,method='POST' if payload else 'GET',headers={'Authorization':f'Bearer {TOKEN}','Accept':'application/vnd.github+json','User-Agent':'profile-stats'})
    data=json.dumps(payload).encode() if payload else None
    if data: req.add_header('Content-Type','application/json')
    with urllib.request.urlopen(req,data=data) as r:return json.load(r)
def esc(s):return html.escape(str(s),quote=True)
def start(w,h,t):return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><rect width="100%" height="100%" rx="14" fill="#0d1117"/><text x="28" y="34" fill="#f0f6fc" font-family="Arial" font-size="16" font-weight="700">{esc(t)}</text>'
user=api(f'https://api.github.com/users/{USER}')
repos=api(f'https://api.github.com/users/{USER}/repos?per_page=100&sort=updated')
public=[r for r in repos if not r.get('fork') and not r.get('private')]
stars=sum(r.get('stargazers_count',0) for r in repos)
langs={}
for r in repos:
    try:
        for k,v in api(r['languages_url']).items():langs[k]=langs.get(k,0)+v
    except Exception:pass
langs=dict(sorted(langs.items(),key=lambda x:x[1],reverse=True)[:8])
gql='query($login:String!){user(login:$login){contributionsCollection{totalCommitContributions totalIssueContributions totalPullRequestContributions contributionCalendar{totalContributions weeks{contributionDays{date contributionCount}}}}}}'
g=api('https://api.github.com/graphql',{'query':gql,'variables':{'login':USER}})['data']['user']['contributionsCollection']; cal=g['contributionCalendar']; days=[d for w in cal['weeks'] for d in w['contributionDays']][-371:]
s=start(900,150,'GITHUB TELEMETRY'); metrics=[('REPOSITORIES',len(repos)),('PUBLIC',len(public)),('STARS',stars),('FOLLOWERS',user.get('followers',0)),('CONTRIBUTIONS',cal['totalContributions'])]
for i,(lab,val) in enumerate(metrics):
 x=28+i*174;s+=f'<text x="{x}" y="78" fill="#8b949e" font-family="Arial" font-size="11">{lab}</text><text x="{x}" y="112" fill="#58a6ff" font-family="Arial" font-size="27" font-weight="700">{val:,}</text>'
(OUT/'telemetry.svg').write_text(s+'</svg>',encoding='utf-8')
s=start(900,300,'LANGUAGE DISTRIBUTION'); total=max(sum(langs.values()),1); y=68
for lang,val in langs.items():
 pct=val/total;width=int(360*pct);s+=f'<text x="28" y="{y}" fill="#c9d1d9" font-family="Arial" font-size="12">{esc(lang)}</text><rect x="150" y="{y-11}" width="360" height="14" rx="7" fill="#21262d"/><rect x="150" y="{y-11}" width="{max(width,3)}" height="14" rx="7" fill="#58a6ff"/><text x="530" y="{y}" fill="#8b949e" font-family="Arial" font-size="11">{pct*100:.1f}%</text>';y+=28
(OUT/'languages.svg').write_text(s+'</svg>',encoding='utf-8')
s=start(900,180,'CONTRIBUTION MATRIX');sx,sy,cell,gap=28,62,10,3;fills=['#161b22','#0e4429','#006d32','#26a641','#39d353']
for idx,d in enumerate(days):
 week,dow=idx//7,idx%7;x=sx+week*(cell+gap);y=sy+dow*(cell+gap);n=d['contributionCount'];lvl=0 if n==0 else 1 if n<3 else 2 if n<6 else 3 if n<10 else 4;s+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="2" fill="{fills[lvl]}"/>'
s+=f'<text x="28" y="158" fill="#8b949e" font-family="Arial" font-size="11">{cal["totalContributions"]:,} contributions in the last year</text></svg>'; (OUT/'activity.svg').write_text(s,encoding='utf-8')
ach=[('TOTAL CONTRIBUTIONS',cal['totalContributions']),('COMMITS',g['totalCommitContributions']),('PULL REQUESTS',g['totalPullRequestContributions']),('ISSUES',g['totalIssueContributions']),('REPOSITORIES',len(repos)),('PUBLIC PROJECTS',len(public))]
s=start(900,240,'ENGINEERING ACHIEVEMENTS')
for i,(lab,val) in enumerate(ach):
 col,row=i%3,i//3;x=28+col*292;y=72+row*76;s+=f'<rect x="{x}" y="{y}" width="265" height="58" rx="9" fill="#161b22" stroke="#30363d"/><text x="{x+16}" y="{y+21}" fill="#8b949e" font-family="Arial" font-size="10">{esc(lab)}</text><text x="{x+16}" y="{y+46}" fill="#58a6ff" font-family="Arial" font-size="20" font-weight="700">{val:,}</text>'
(OUT/'achievements.svg').write_text(s+'</svg>',encoding='utf-8')
