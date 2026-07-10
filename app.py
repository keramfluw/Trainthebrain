import streamlit as st
from datetime import date, time

st.set_page_config(
    page_title="Clever College & CCData GmbH Aviation Academy",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded",
)

BRAND_BLUE = "#0B2A4A"
BRAND_GOLD = "#D6A84F"
LIGHT_BG = "#F5F7FA"

st.markdown(
    f"""
    <style>
    .stApp {{ background: {LIGHT_BG}; }}
    .hero {{
        background: linear-gradient(135deg, {BRAND_BLUE}, #123f6d);
        padding: 2.2rem;
        border-radius: 22px;
        color: white;
        margin-bottom: 1.5rem;
    }}
    .hero h1 {{ font-size: 2.6rem; margin-bottom: .25rem; }}
    .hero p {{ font-size: 1.08rem; opacity: .95; max-width: 900px; }}
    .badge {{
        display: inline-block;
        background: {BRAND_GOLD};
        color: {BRAND_BLUE};
        padding: .25rem .7rem;
        border-radius: 999px;
        font-weight: 700;
        margin-bottom: .75rem;
    }}
    .card {{
        background: white;
        border: 1px solid #E4E8EE;
        border-radius: 18px;
        padding: 1.15rem;
        box-shadow: 0 8px 22px rgba(11,42,74,.06);
        height: 100%;
    }}
    .course-title {{ color: {BRAND_BLUE}; font-size: 1.25rem; font-weight: 800; }}
    .price {{ color: {BRAND_GOLD}; font-size: 1.1rem; font-weight: 800; }}
    .small {{ color: #546070; font-size: .92rem; }}
    div.stButton > button:first-child {{
        background: {BRAND_BLUE};
        color: white;
        border-radius: 999px;
        border: 0;
        padding: .55rem 1.1rem;
        font-weight: 700;
    }}
    div.stButton > button:first-child:hover {{
        background: #16466f;
        color: white;
        border: 0;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

COURSES = [
    {
        "title": "Luftfahrttechnik Grundlagen",
        "category": "Technik",
        "location": "Hammah / Stade",
        "duration": "3 Tage",
        "price": 890,
        "level": "Einsteiger",
        "description": "Praxisnaher Einstieg in Baugruppen, Komponenten, Dokumentation und Qualitätslogik der Luftfahrtindustrie.",
    },
    {
        "title": "Aerospace Material- und Lagerprozesse",
        "category": "Logistik",
        "location": "Hamburg",
        "duration": "2 Tage",
        "price": 690,
        "level": "Fachkraft",
        "description": "Materialfluss, Teileidentifikation, Rückverfolgbarkeit und sichere Lagerprozesse für Luft- und Raumfahrtmaterial.",
    },
    {
        "title": "Qualitätssicherung Aviation",
        "category": "Qualität",
        "location": "Bremen",
        "duration": "4 Tage",
        "price": 1190,
        "level": "Fortgeschritten",
        "description": "Auditfähigkeit, Fehlerdokumentation, Prüfprozesse und qualitätsrelevante Nachweise im Aerospace-Umfeld.",
    },
    {
        "title": "Technische Dokumentation & Compliance",
        "category": "Dokumentation",
        "location": "München",
        "duration": "2 Tage",
        "price": 760,
        "level": "Fortgeschritten",
        "description": "Umgang mit Zeichnungen, Arbeitsanweisungen, Nachweisen und revisionssicherer Dokumentation.",
    },
]

LOCATIONS = ["Deutschlandweit", "Hammah / Stade", "Hamburg", "Bremen", "München", "Berlin", "Köln", "Frankfurt"]
CATEGORIES = ["Alle", "Technik", "Logistik", "Qualität", "Dokumentation"]

if "bookings" not in st.session_state:
    st.session_state.bookings = []
if "trainers" not in st.session_state:
    st.session_state.trainers = []

st.markdown(
    """
    <div class="hero">
      <div class="badge">CCData GmbH Aviation Academy · Aviation Training</div>
      <h1>Lehrgänge im Bereich Luftfahrt buchen</h1>
      <p>Eine digitale Akademie-Plattform für Endanwender, Unternehmen und Ausbilder: Kurse finden, Buchungsanfragen senden und Trainer-Verfügbarkeiten deutschlandweit strukturieren.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.image("https://www.clever-college.com/wp-content/uploads/2023/03/cropped-clever-college-logo-1.png", use_container_width=True)
    st.markdown("### Navigation")
    page = st.radio("Bereich wählen", ["Lehrgänge buchen", "Ausbilder registrieren", "Admin Cockpit"], label_visibility="collapsed")
    st.markdown("---")
    st.caption("Prototyp für GitHub/Streamlit Hosting. Daten werden in dieser Version in der Session gespeichert.")

if page == "Lehrgänge buchen":
    st.subheader("Lehrgangskatalog")
    c1, c2, c3 = st.columns([1.2, 1, 1])
    with c1:
        search = st.text_input("Suche", placeholder="z. B. Qualität, Lager, Dokumentation")
    with c2:
        category = st.selectbox("Kategorie", CATEGORIES)
    with c3:
        location = st.selectbox("Ort", LOCATIONS)

    filtered = []
    for course in COURSES:
        matches_search = not search or search.lower() in (course["title"] + course["description"] + course["category"]).lower()
        matches_category = category == "Alle" or course["category"] == category
        matches_location = location == "Deutschlandweit" or course["location"] == location
        if matches_search and matches_category and matches_location:
            filtered.append(course)

    if not filtered:
        st.info("Keine passenden Lehrgänge gefunden. Bitte Filter anpassen.")

    for i in range(0, len(filtered), 2):
        cols = st.columns(2)
        for col, course in zip(cols, filtered[i:i+2]):
            with col:
                st.markdown(
                    f"""
                    <div class="card">
                      <div class="course-title">{course['title']}</div>
                      <p>{course['description']}</p>
                      <p class="small">📍 {course['location']} · ⏱ {course['duration']} · Niveau: {course['level']}</p>
                      <p class="price">{course['price']} € zzgl. MwSt.</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                if st.button(f"Buchungsanfrage: {course['title']}", key=f"book_{course['title']}"):
                    st.session_state.selected_course = course["title"]
                    st.success("Lehrgang für die Buchungsanfrage ausgewählt.")

    st.markdown("---")
    st.subheader("Buchungsanfrage senden")
    with st.form("booking_form"):
        selected_course = st.selectbox("Gewünschter Lehrgang", [c["title"] for c in COURSES], index=0)
        name = st.text_input("Name")
        email = st.text_input("E-Mail")
        company = st.text_input("Unternehmen / Organisation")
        preferred_date = st.date_input("Wunschtermin", value=date.today())
        participants = st.number_input("Teilnehmerzahl", min_value=1, max_value=50, value=1)
        note = st.text_area("Hinweise", placeholder="z. B. Inhouse-Schulung, besonderer Ort, gewünschter Schwerpunkt")
        submitted = st.form_submit_button("Anfrage speichern")

    if submitted:
        st.session_state.bookings.append({
            "Lehrgang": selected_course,
            "Name": name,
            "E-Mail": email,
            "Unternehmen": company,
            "Wunschtermin": str(preferred_date),
            "Teilnehmer": participants,
            "Hinweis": note,
        })
        st.success("Die Buchungsanfrage wurde im Prototyp gespeichert.")

elif page == "Ausbilder registrieren":
    st.subheader("Ausbilderprofil anlegen")
    with st.form("trainer_form"):
        col1, col2 = st.columns(2)
        with col1:
            trainer_name = st.text_input("Name des Ausbilders")
            trainer_email = st.text_input("E-Mail")
            phone = st.text_input("Telefon")
            qualification = st.multiselect("Qualifikationsbereiche", ["Luftfahrttechnik", "Logistik", "Qualität", "Dokumentation", "Arbeitssicherheit", "Fertigung"])
        with col2:
            cities = st.multiselect("Einsatzorte in Deutschland", LOCATIONS[1:])
            available_from = st.date_input("Verfügbar ab", value=date.today())
            available_until = st.date_input("Verfügbar bis", value=date.today())
            time_window = st.selectbox("Zeitrahmen", ["Ganztägig", "Vormittag", "Nachmittag", "Abend"])
        bio = st.text_area("Kurzprofil", placeholder="Erfahrung, Zertifikate, Branchenschwerpunkte")
        trainer_submit = st.form_submit_button("Ausbilder registrieren")

    if trainer_submit:
        st.session_state.trainers.append({
            "Name": trainer_name,
            "E-Mail": trainer_email,
            "Telefon": phone,
            "Qualifikationen": ", ".join(qualification),
            "Orte": ", ".join(cities),
            "Von": str(available_from),
            "Bis": str(available_until),
            "Zeitrahmen": time_window,
            "Profil": bio,
        })
        st.success("Das Ausbilderprofil wurde im Prototyp gespeichert.")

    st.markdown("---")
    st.subheader("Registrierte Ausbilder")
    if st.session_state.trainers:
        st.dataframe(st.session_state.trainers, use_container_width=True)
    else:
        st.info("Noch keine Ausbilder registriert.")

else:
    st.subheader("Admin Cockpit")
    k1, k2, k3 = st.columns(3)
    k1.metric("Lehrgänge", len(COURSES))
    k2.metric("Buchungsanfragen", len(st.session_state.bookings))
    k3.metric("Ausbilder", len(st.session_state.trainers))

    st.markdown("### Buchungsanfragen")
    if st.session_state.bookings:
        st.dataframe(st.session_state.bookings, use_container_width=True)
    else:
        st.info("Noch keine Buchungsanfragen vorhanden.")

    st.markdown("### Ausbilderdaten")
    if st.session_state.trainers:
        st.dataframe(st.session_state.trainers, use_container_width=True)
    else:
        st.info("Noch keine Ausbilderdaten vorhanden.")

st.markdown("---")
st.caption("© CCData GmbH Aviation Academy-Prototyp · Fokus: Luftfahrt, Weiterbildung, Ausbildernetzwerk, Deutschland")
