from enum import StrEnum


class Language(StrEnum):
    EN = "en"
    FR = "fr"
    DE = "de"
    ES = "es"
    IT = "it"
    PT = "pt"
    NL = "nl"
    UNKNOWN = "unknown"


_LANGUAGE_HINTS: dict[Language, set[str]] = {
    Language.FR: {"pourquoi", "marge", "chuté", "retard", "fournisseur", "incident", "risque"},
    Language.DE: {"warum", "marge", "gesunken", "lieferant", "vorfall", "risiko", "verzögerung"},
    Language.ES: {"por qué", "margen", "proveedor", "incidente", "riesgo", "retraso"},
    Language.IT: {"perché", "margine", "fornitore", "incidente", "rischio", "ritardo"},
    Language.PT: {"por que", "margem", "fornecedor", "incidente", "risco", "atraso"},
    Language.NL: {"waarom", "marge", "leverancier", "incident", "risico", "vertraging"},
    Language.EN: {"why", "margin", "supplier", "incident", "risk", "delay", "root cause"},
}


def detect_language(text: str) -> Language:
    normalized = text.lower()
    scores = {
        language: sum(1 for hint in hints if hint in normalized)
        for language, hints in _LANGUAGE_HINTS.items()
    }
    language, score = max(scores.items(), key=lambda item: item[1])
    return language if score > 0 else Language.EN


def localize_synthesis(language: Language) -> str:
    messages = {
        Language.FR: "Synthèse IA locale: les signaux indiquent une corrélation probable entre les incidents IT, les changements récents et l'impact service.",
        Language.DE: "Lokale KI-Zusammenfassung: Die Signale zeigen wahrscheinlich einen Zusammenhang zwischen IT-Vorfällen, jüngsten Änderungen und Service-Auswirkungen.",
        Language.ES: "Síntesis IA local: las señales indican una correlación probable entre incidentes de TI, cambios recientes e impacto en el servicio.",
        Language.IT: "Sintesi IA locale: i segnali indicano una probabile correlazione tra incidenti IT, modifiche recenti e impatto sul servizio.",
        Language.PT: "Síntese de IA local: os sinais indicam uma correlação provável entre incidentes de TI, mudanças recentes e impacto no serviço.",
        Language.NL: "Lokale AI-samenvatting: de signalen wijzen waarschijnlijk op een verband tussen IT-incidenten, recente wijzigingen en service-impact.",
        Language.EN: "Local AI synthesis: the signals indicate a probable correlation between IT incidents, recent changes, and service impact.",
    }
    return messages.get(language, messages[Language.EN])
