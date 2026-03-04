import json

# (id, type, name, x, y, w, h)
NODES = [
    ("an_start",       "UMLInitialNode",       "Start",                          340,  20, 20, 20),
    ("aa_open",        "UMLAction",            "Open Lets_Study",                270,  70,180, 36),
    ("aa_signin",      "UMLAction",            "Sign in with Google",            270, 130,180, 36),
    ("ad_auth",        "UMLDecisionNode",      "Authenticated?",                 320, 195, 80, 40),
    ("aa_dashboard",   "UMLAction",            "Load Dashboard",                 270, 265,180, 36),
    ("ad_choice",      "UMLDecisionNode",      "Choose Activity",                320, 330, 80, 40),

    # Timer branch
    ("aa_select_sub",  "UMLAction",            "Select Subject",                  20, 410,160, 36),
    ("aa_start_timer", "UMLAction",            "Click Start Timer",               20, 465,160, 36),
    ("aa_insert_start","UMLAction",            "INSERT start event",              20, 520,160, 36),
    ("aa_running",     "UMLAction",            "Timer Running",                   20, 575,160, 36),
    ("ad_timer",       "UMLDecisionNode",      "Student Action?",                 65, 640, 80, 40),
    ("aa_pause",       "UMLAction",            "INSERT pause event",               20, 705,160, 36),
    ("aa_paused",      "UMLAction",            "Timer Paused",                    20, 760,160, 36),
    ("ad_resume",      "UMLDecisionNode",      "Resume or Stop?",                 65, 820, 80, 40),
    ("aa_resume",      "UMLAction",            "INSERT resume event",              20, 880,160, 36),
    ("aa_stop",        "UMLAction",            "INSERT stop event",               20, 935,160, 36),
    ("aa_derive",      "UMLAction",            "deriveFocusState",                20, 990,160, 36),
    ("aa_saved",       "UMLAction",            "Session Saved",                   20,1045,160, 36),

    # Analytics branch
    ("aa_fetch",       "UMLAction",            "Fetch all focus_events",         220, 410,180, 36),
    ("aa_segments",    "UMLAction",            "eventsToSegments",               220, 465,180, 36),
    ("aa_totals",      "UMLAction",            "Compute totals",                 220, 520,180, 36),
    ("aa_score",       "UMLAction",            "Calculate Productivity Score",   220, 575,180, 36),
    ("aa_insights",    "UMLAction",            "Generate Smart Insights",        220, 630,180, 36),
    ("aa_charts",      "UMLAction",            "Render Charts & Calendar",       220, 685,180, 36),
    ("ad_ai",          "UMLDecisionNode",      "Open AI Coach?",                 265, 750, 80, 40),
    ("aa_ai_send",     "UMLAction",            "Send analytics to Groq",         220, 815,180, 36),
    ("aa_ai_display",  "UMLAction",            "Display AI Advice",              220, 870,180, 36),

    # Notes branch
    ("aa_notes_lib",   "UMLAction",            "View Notes Library",             430, 410,180, 36),
    ("aa_open_editor", "UMLAction",            "Open BlockNote Editor",          430, 465,180, 36),
    ("aa_autosave",    "UMLAction",            "Debounced auto-save to DB",      430, 520,180, 36),
    ("aa_export",      "UMLAction",            "Export Note (md/html/doc)",      430, 575,180, 36),

    # PDF branch
    ("aa_upload_pdf",  "UMLAction",            "Upload PDF",                     640, 410,180, 36),
    ("aa_chunk",       "UMLAction",            "Chunk PDF text",                 640, 465,180, 36),
    ("aa_embed",       "UMLAction",            "Generate Embeddings",            640, 520,180, 36),
    ("aa_cluster",     "UMLAction",            "K-Means Clustering",             640, 575,180, 36),
    ("aa_label",       "UMLAction",            "LLM Topic Labelling (Groq)",     640, 630,180, 36),
    ("aa_dag",         "UMLAction",            "Build DAG (Prereq Graph)",       640, 685,180, 36),
    ("aa_store",       "UMLAction",            "Store in Supabase pgvector",     640, 740,180, 36),
    ("aa_display_dag", "UMLAction",            "Display Clusters/Topics/DAG",    640, 795,180, 36),

    # Checklist branch
    ("aa_checklist",   "UMLAction",            "View Daily Checklist",           850, 410,180, 36),
    ("aa_add_task",    "UMLAction",            "Add Task",                       850, 465,180, 36),
    ("aa_toggle_task", "UMLAction",            "Toggle Task Complete",           850, 520,180, 36),

    ("aa_logout",      "UMLAction",            "Logout",                         340,1120,180, 36),
    ("an_end",         "UMLActivityFinalNode", "End",                            340,1180, 20, 20),
]

FLOWS = [
    ("f1", "an_start","aa_open",""),
    ("f2", "aa_open","aa_signin",""),
    ("f3", "aa_signin","ad_auth",""),
    ("f4", "ad_auth","aa_signin","No"),
    ("f5", "ad_auth","aa_dashboard","Yes"),
    ("f6", "aa_dashboard","ad_choice",""),
    # Timer
    ("f7",  "ad_choice","aa_select_sub","Start Session"),
    ("f8",  "aa_select_sub","aa_start_timer",""),
    ("f9",  "aa_start_timer","aa_insert_start",""),
    ("f10", "aa_insert_start","aa_running",""),
    ("f11", "aa_running","ad_timer",""),
    ("f12", "ad_timer","aa_pause","Pause"),
    ("f13", "aa_pause","aa_paused",""),
    ("f14", "aa_paused","ad_resume",""),
    ("f15", "ad_resume","aa_resume","Resume"),
    ("f16", "aa_resume","aa_running",""),
    ("f17", "ad_resume","aa_stop","Stop"),
    ("f18", "ad_timer","aa_stop","Stop"),
    ("f19", "aa_stop","aa_derive",""),
    ("f20", "aa_derive","aa_saved",""),
    ("f21", "aa_saved","ad_choice",""),
    # Analytics
    ("f22", "ad_choice","aa_fetch","View Analytics"),
    ("f23", "aa_fetch","aa_segments",""),
    ("f24", "aa_segments","aa_totals",""),
    ("f25", "aa_totals","aa_score",""),
    ("f26", "aa_score","aa_insights",""),
    ("f27", "aa_insights","aa_charts",""),
    ("f28", "aa_charts","ad_ai",""),
    ("f29", "ad_ai","aa_ai_send","Yes"),
    ("f30", "aa_ai_send","aa_ai_display",""),
    ("f31", "aa_ai_display","ad_choice",""),
    ("f32", "ad_ai","ad_choice","No"),
    # Notes
    ("f33", "ad_choice","aa_notes_lib","Open Notes"),
    ("f34", "aa_notes_lib","aa_open_editor",""),
    ("f35", "aa_open_editor","aa_autosave",""),
    ("f36", "aa_open_editor","aa_export",""),
    ("f37", "aa_export","ad_choice",""),
    # PDF
    ("f38", "ad_choice","aa_upload_pdf","Upload PDF"),
    ("f39", "aa_upload_pdf","aa_chunk",""),
    ("f40", "aa_chunk","aa_embed",""),
    ("f41", "aa_embed","aa_cluster",""),
    ("f42", "aa_cluster","aa_label",""),
    ("f43", "aa_label","aa_dag",""),
    ("f44", "aa_dag","aa_store",""),
    ("f45", "aa_store","aa_display_dag",""),
    ("f46", "aa_display_dag","ad_choice",""),
    # Checklist
    ("f47", "ad_choice","aa_checklist","Checklist"),
    ("f48", "aa_checklist","aa_add_task",""),
    ("f49", "aa_checklist","aa_toggle_task",""),
    ("f50", "aa_add_task","ad_choice",""),
    ("f51", "aa_toggle_task","ad_choice",""),
    # Logout
    ("f52", "ad_choice","aa_logout","Logout"),
    ("f53", "aa_logout","an_end",""),
]

node_pos = {nid:(x,y,w,h) for nid,_,_,x,y,w,h in NODES}

model_els = []
view_els  = []

for nid, ntype, nname, x, y, w, h in NODES:
    model_els.append({"_type":ntype,"_id":nid,"_parent":{"$ref":"M4"},"name":nname})
    vtype = ntype+"View"
    view_els.append({"_type":vtype,"_id":"v_"+nid,"_parent":{"$ref":"D4"},"model":{"$ref":nid},"left":x,"top":y,"width":w,"height":h})

for fid, src, tgt, guard in FLOWS:
    entry = {"_type":"UMLControlFlow","_id":fid,"_parent":{"$ref":"M4"},"source":{"$ref":src},"target":{"$ref":tgt}}
    if guard: entry["guard"] = guard
    model_els.append(entry)

    sx,sy,sw,sh = node_pos[src]
    tx,ty,tw,th = node_pos[tgt]
    pts = f"{sx+sw//2},{sy+sh};{tx+tw//2},{ty}"
    ventry = {
        "_type":"UMLControlFlowView","_id":"vf_"+fid,"_parent":{"$ref":"D4"},
        "model":{"$ref":fid},
        "end1":{"reference":{"$ref":"v_"+src},"_type":"EdgeParamView"},
        "end2":{"reference":{"$ref":"v_"+tgt},"_type":"EdgeParamView"},
        "points":pts
    }
    if guard: ventry["label"] = guard
    view_els.append(ventry)

mdj = {
    "_type":"Project","_id":"P4","name":"Lets_Study - Activity Diagram",
    "ownedElements":[{
        "_type":"UMLModel","_id":"M4","name":"Activity Model","_parent":{"$ref":"P4"},
        "ownedElements": model_els + [{
            "_type":"UMLActivityDiagram","_id":"D4","_parent":{"$ref":"M4"},
            "name":"Lets_Study Activity Diagram","defaultDiagram":True,
            "ownedViews": view_els
        }]
    }]
}

with open("4_ActivityDiagram.mdj","w",encoding="utf-8") as f:
    json.dump(mdj,f,indent=2,ensure_ascii=False)
print("✅ 4_ActivityDiagram.mdj done!")