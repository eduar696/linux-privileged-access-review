from analyzer.users import get_all_users
from analyzer.groups import get_user_privileged_groups
from analyzer.risk import calculate_risk
from analyzer.report import print_terminal_report, export_json_report


def run_scan():
    users = get_all_users()
    report_data = []
    
    for u in users:
        priv_groups = get_user_privileged_groups(u['username'])
        risk = calculate_risk(u, priv_groups)
        
        if risk['score'] > 0:
            report_data.append({
                "username": u['username'],
                "risk": risk
            })
    
    print_terminal_report(report_data)
    
    # Exportar siempre para tener evidencia
    if report_data:
        export_json_report(report_data)


if __name__ == "__main__":
    run_scan()
