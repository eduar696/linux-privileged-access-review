def calculate_risk(user_data, privileged_groups):
    """
    Calcula un score de riesgo simple.
    """
    score = 0
    reasons = []

    # 1. Riesgo por grupos (si está en grupos privilegiados)
    if privileged_groups:
        score += 40
        reasons.append(f"Privileged groups: {', '.join(privileged_groups)}")
    
    # 2. Riesgo por inactividad (esto es lógico, se puede mejorar el cálculo luego)
    # Por ahora, si 'last_login' es 'Nunca', penalizamos fuerte
    if user_data['last_login'] == "Nunca":
        score += 30
        reasons.append("Never logged in")
    
    # Categorización
    if score >= 70:
        level = "HIGH"
    elif score >= 40:
        level = "MEDIUM"
    else:
        level = "LOW"
        
    return {"score": score, "level": level, "reasons": reasons}
