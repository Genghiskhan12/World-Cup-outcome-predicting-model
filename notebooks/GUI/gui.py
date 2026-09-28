from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import numpy as np
import pickle

# The GUI lives in notebooks/GUI, while the data directory is at the
# repository root.
DATA=Path(__file__).resolve().parents[2]/'data/processed/matches_1930_2022_cleaned.csv'
MODEL=Path(__file__).resolve().parents[2]/'model.pkl'
LABELS={0:'Team A win',1:'Draw',2:'Team B win'}

def prepare():
 with MODEL.open('rb') as f: artifact=pickle.load(f)
 return artifact['snapshots'], artifact['model'], artifact['features'], artifact['labels']

def launch():
 snaps,model,COLS,LABELS=prepare(); teams=sorted(snaps); root=tk.Tk(); root.title('World Cup Match Simulator'); f=ttk.Frame(root,padding=20); f.pack(fill='both',expand=True); ttk.Label(f,text='World Cup Match Simulator',font=('Arial',18,'bold')).pack(pady=10); v={k:tk.StringVar() for k in ('Team A','Year A','Team B','Year B')}; boxes={}
 for k in v:
  ttk.Label(f,text=k).pack(); boxes[k]=ttk.Combobox(f,textvariable=v[k],state='readonly',width=35); boxes[k].pack();
 boxes['Team A']['values']=teams; boxes['Team B']['values']=teams; v['Team A'].set(teams[0]); v['Team B'].set(teams[1]); ha,hb=tk.BooleanVar(),tk.BooleanVar(); ttk.Checkbutton(f,text='Team A is host',variable=ha).pack(); ttk.Checkbutton(f,text='Team B is host',variable=hb).pack(); out=ttk.Label(f,text='',justify='center',font=('Arial',12)); out.pack(pady=10)
 def clear(*_): out.config(text='')
 def refresh(e=None):
  for t,y in (('Team A','Year A'),('Team B','Year B')): z=sorted({q['year'] for q in snaps[v[t].get()]}); boxes[y]['values']=z; v[y].set(z[-1]); clear()
 boxes['Team A'].bind('<<ComboboxSelected>>',refresh); boxes['Team B'].bind('<<ComboboxSelected>>',refresh); refresh()
 def run():
  if v['Team A'].get()==v['Team B'].get() or ha.get() and hb.get(): messagebox.showerror('Invalid selection','Choose different teams and at most one host.'); return
  default={'elo':1500.,'goals_scored_last_5':0,'goals_conceded_last_5':0,'win_rate_last_5':0,'post_wc_rating':0,'rating_available':0}; aa=[q for q in snaps[v['Team A'].get()] if q['year']<=int(v['Year A'].get())]; bb=[q for q in snaps[v['Team B'].get()] if q['year']<=int(v['Year B'].get())]; a=aa[-1] if aa else default; b=bb[-1] if bb else default
  row=pd.DataFrame([{'elo_diff':a['elo']-b['elo'],'expected_A':1/(1+10**((b['elo']-a['elo'])/400)),'win_rate_diff':a['win_rate_last_5']-b['win_rate_last_5'],'goals_scored_diff':a['goals_scored_last_5']-b['goals_scored_last_5'],'goals_conceded_diff':b['goals_conceded_last_5']-a['goals_conceded_last_5'],'A_win_rate_last_5':a['win_rate_last_5'],'B_win_rate_last_5':b['win_rate_last_5'],'is_host_A':int(ha.get()),'is_host_B':int(hb.get()),'A_wc_rating':a['post_wc_rating'],'B_wc_rating':b['post_wc_rating'],'post_wc_rating_diff':a['post_wc_rating']-b['post_wc_rating'],'playoff_rating_available':a['rating_available']+b['rating_available']}],columns=COLS); p=model.predict_proba(row)[0]; out.config(text=f'Team A win: {p[0]:.1%}\nDraw: {p[1]:.1%}\nTeam B win: {p[2]:.1%}\n\nPrediction: {LABELS[int(np.argmax(p))]}')
 btn=ttk.Button(f,text='Simulate Match',command=run); btn.pack(pady=5); [boxes[k].bind('<<ComboboxSelected>>',clear,add='+') for k in boxes]; ha.trace_add('write',clear); hb.trace_add('write',clear); root.mainloop()


if __name__ == '__main__':
 launch()
