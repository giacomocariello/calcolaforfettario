import streamlit as st

st.title("Calcola gross-netto del forfettario")

st.number_input("Aliquota INPS (%)", key="inps_pct", value=24.09)
st.number_input("Imposta sostitutiva (%)", key="sostitutiva_pct", value=5)
st.number_input("Coefficiente di redditività (%)", key="imponibile_pct", value=67)

giorni_lavorativi = 254

def worked_days():
    return giorni_lavorativi-st.session_state.holidays

def gross_monthly():
    return int(st.session_state.gross_total/12)

def gross_daily():
    return int(st.session_state.gross_total/st.session_state.worked_days)

def gross_hourly():
    return int(gross_daily()/8)

def inps_total_from_gross():
    return int(st.session_state.gross_total*(float(st.session_state.imponibile_pct)/100)*(float(st.session_state.inps_pct)/100))

def tax_total_pct():
    return ((float(st.session_state.inps_pct)/100)+(float(st.session_state.sostitutiva_pct)/100))*(float(st.session_state.imponibile_pct)/100)

def gross_from_net():
    return int(st.session_state.net_total/(1-tax_total_pct()))

def inps_total_from_net():
    return int(gross_from_net()*(float(st.session_state.inps_pct)/100))

def sostitutiva_total_from_gross():
    return int(st.session_state.gross_total*(float(st.session_state.imponibile_pct)/100)*(float(st.session_state.sostitutiva_pct)/100))

def sostitutiva_total_from_net():
    return int(gross_from_net()*(float(st.session_state.sostitutiva_pct)/100))

def net_total():
    return int(st.session_state.gross_total-inps_total_from_gross()-sostitutiva_total_from_gross())

def net_monthly():
    return int(net_total()/12)

def net_daily():
    return int(net_total()/st.session_state.worked_days)

def net_hourly():
    return int(net_daily()/8)

def on_change_worked_days():
    st.session_state.holidays = giorni_lavorativi-st.session_state.worked_days
    st.session_state.gross_daily = gross_daily()
    st.session_state.gross_hourly = gross_hourly()
    st.session_state.net_daily = net_daily()
    st.session_state.net_hourly = net_hourly()

def on_change_holidays():
    st.session_state.worked_days = giorni_lavorativi-st.session_state.holidays
    st.session_state.gross_daily = gross_daily()
    st.session_state.gross_hourly = gross_hourly()
    st.session_state.net_daily = net_daily()
    st.session_state.net_hourly = net_hourly()

def on_change_gross_total():
    st.session_state.gross_monthly = gross_monthly()
    st.session_state.gross_daily = gross_daily()
    st.session_state.gross_hourly = gross_hourly()
    st.session_state.inps_total = inps_total_from_gross()
    st.session_state.sostitutiva_total = sostitutiva_total_from_gross()
    st.session_state.net_total = net_total()
    st.session_state.net_monthly = net_monthly()
    st.session_state.net_daily = net_daily()
    st.session_state.net_hourly = net_hourly()

def on_change_gross_monthly():
    st.session_state.gross_total = st.session_state.gross_monthly*12
    st.session_state.gross_daily = gross_daily()
    st.session_state.gross_hourly = gross_hourly()
    st.session_state.inps_total = inps_total_from_gross()
    st.session_state.sostitutiva_total = sostitutiva_total_from_gross()
    st.session_state.net_total = net_total()
    st.session_state.net_daily = net_daily()
    st.session_state.net_hourly = net_hourly()

def on_change_gross_daily():
    st.session_state.gross_total = st.session_state.gross_daily*st.session_state.worked_days
    st.session_state.gross_monthly = gross_monthly()
    st.session_state.gross_hourly = gross_hourly()
    st.session_state.inps_total = inps_total_from_gross()
    st.session_state.sostitutiva_total = sostitutiva_total_from_gross()
    st.session_state.net_total = net_total()
    st.session_state.net_monthly = net_monthly()
    st.session_state.net_daily = net_daily()
    st.session_state.net_hourly = net_hourly()

def on_change_gross_hourly():
    st.session_state.gross_total = st.session_state.gross_hourly*8*st.session_state.worked_days
    st.session_state.gross_monthly = gross_monthly()
    st.session_state.gross_daily = gross_daily()
    st.session_state.inps_total = inps_total_from_gross()
    st.session_state.sostitutiva_total = sostitutiva_total_from_gross()
    st.session_state.net_total = net_total()
    st.session_state.net_monthly = net_monthly()
    st.session_state.net_daily = net_daily()
    st.session_state.net_hourly = net_hourly()

def on_change_net_total():
    st.session_state.inps_total = inps_total_from_net()
    st.session_state.sostitutiva_total = sostitutiva_total_from_net()
    st.session_state.gross_total = gross_from_net()
    st.session_state.gross_monthly = gross_monthly()
    st.session_state.gross_daily = gross_daily()
    st.session_state.gross_hourly = gross_hourly()
    st.session_state.net_monthly = net_monthly()
    st.session_state.net_daily = net_daily()
    st.session_state.net_hourly = net_hourly()

def on_change_net_monthly():
    st.session_state.net_total = st.session_state.net_monthly*12
    st.session_state.inps_total = inps_total_from_net()
    st.session_state.sostitutiva_total = sostitutiva_total_from_net()
    st.session_state.gross_total = gross_from_net()
    st.session_state.gross_monthly = gross_monthly()
    st.session_state.gross_daily = gross_daily()
    st.session_state.gross_hourly = gross_hourly()
    st.session_state.net_daily = net_daily()
    st.session_state.net_hourly = net_hourly()

def on_change_net_daily():
    st.session_state.net_total = st.session_state.net_daily*st.session_state.worked_days
    st.session_state.inps_total = inps_total_from_net()
    st.session_state.sostitutiva_total = sostitutiva_total_from_net()
    st.session_state.gross_total = gross_from_net()
    st.session_state.gross_monthly = gross_monthly()
    st.session_state.gross_daily = gross_daily()
    st.session_state.gross_hourly = gross_hourly()
    st.session_state.net_monthly = net_monthly()
    st.session_state.net_hourly = net_hourly()

def on_change_net_hourly():
    st.session_state.net_total = st.session_state.net_hourly*8*st.session_state.worked_days
    st.session_state.inps_total = inps_total_from_net()
    st.session_state.sostitutiva_total = sostitutiva_total_from_net()
    st.session_state.gross_total = gross_from_net()
    st.session_state.gross_monthly = gross_monthly()
    st.session_state.gross_daily = gross_daily()
    st.session_state.gross_hourly = gross_hourly()
    st.session_state.net_monthly = net_monthly()
    st.session_state.net_daily = net_daily()

if 'holidays' not in st.session_state:
    st.session_state.holidays = 30

if 'worked_days' not in st.session_state:
    st.session_state.worked_days = worked_days()

if 'gross_total' not in st.session_state:
    st.session_state.gross_total = 60000

if 'gross_monthly' not in st.session_state:
    st.session_state.gross_monthly = gross_monthly()

if 'gross_daily' not in st.session_state:
    st.session_state.gross_daily = gross_daily()

if 'gross_hourly' not in st.session_state:
    st.session_state.gross_hourly = gross_hourly()

if 'inps_total' not in st.session_state:
    st.session_state.inps_total = inps_total_from_gross()

if 'sostitutiva_total' not in st.session_state:
    st.session_state.sostitutiva_total = sostitutiva_total_from_gross()

if 'net_total' not in st.session_state:
    st.session_state.net_total = net_total()

if 'net_monthly' not in st.session_state:
    st.session_state.net_monthly = net_monthly()

if 'net_daily' not in st.session_state:
    st.session_state.net_daily = net_daily()

if 'net_hourly' not in st.session_state:
    st.session_state.net_hourly = net_hourly()

st.slider("Giorni di ferie/inattività", key="holidays", min_value=0, max_value=365, step=1, on_change=on_change_holidays)
st.slider("Numero giornate lavorate", key="worked_days", min_value=1, max_value=365, step=1, on_change=on_change_worked_days)
st.slider("Lordo totale", key="gross_total", min_value=0, max_value=85000, step=100, on_change=on_change_gross_total)

st.number_input("INPS totale", key="inps_total")
st.number_input("Imposta sostitutiva totale", key="sostitutiva_total")

st.slider("Lordo mensile", key="gross_monthly", min_value=0, max_value=7100, step=10, on_change=on_change_gross_monthly)
st.slider("Lordo giornata", key="gross_daily", min_value=0, max_value=500, step=5, on_change=on_change_gross_daily)
st.slider("Lordo orario", key="gross_hourly", min_value=0, max_value=200, step=1, on_change=on_change_gross_hourly)

st.slider("Netto totale", key="net_total", min_value=0, max_value=85000, step=100, on_change=on_change_net_total)
st.slider("Netto mensile", key="net_monthly", min_value=0, max_value=7100, step=10 , on_change=on_change_net_monthly)
st.slider("Netto giornata", key="net_daily", min_value=0, max_value=500, step=1, on_change=on_change_net_daily)
st.slider("Netto orario", key="net_hourly", min_value=0, max_value=200, step=1, on_change=on_change_net_hourly)
