from pydantic import BaseModel, Field


class SectorPack(BaseModel):
    key: str
    name: str
    typical_systems: list[str]
    core_entities: list[str]
    anomaly_examples: list[str]
    recommended_connectors: list[str]
    compliance_notes: list[str] = Field(default_factory=list)


SECTOR_PACKS: dict[str, SectorPack] = {
    "civil_engineering": SectorPack(
        key="civil_engineering",
        name="Génie civil / Construction",
        typical_systems=["ERP", "BIM", "GIS", "Project Management", "Procurement", "IoT site sensors"],
        core_entities=["Project", "Site", "Contract", "Subcontractor", "Asset", "Incident", "Risk"],
        anomaly_examples=["retard chantier", "dépassement budget", "risque fournisseur", "incident sécurité"],
        recommended_connectors=["SAP", "Oracle Primavera", "Autodesk/BIM", "SharePoint", "IoT MQTT"],
        compliance_notes=["traçabilité contractuelle", "santé-sécurité", "souveraineté documentaire"],
    ),
    "finance": SectorPack(
        key="finance",
        name="Finance / Banque / Assurance",
        typical_systems=["Core banking", "Risk engine", "CRM", "KYC", "AML", "Data warehouse"],
        core_entities=["Customer", "Account", "Transaction", "Contract", "Risk", "Alert", "Document"],
        anomaly_examples=["fraude", "churn", "risque crédit", "non-conformité KYC", "perte marge"],
        recommended_connectors=["Temenos", "Murex", "Salesforce", "ServiceNow", "Snowflake"],
        compliance_notes=["auditabilité", "GDPR", "DORA", "AML", "segregation of duties"],
    ),
    "it_operations": SectorPack(
        key="it_operations",
        name="IT / Cloud / Support",
        typical_systems=["ITSM", "CMDB", "SIEM", "APM", "Cloud", "Git"],
        core_entities=["Service", "Asset", "Incident", "Change", "Risk", "Employee", "Process"],
        anomaly_examples=["incident majeur", "latence", "fail deployment", "risque sécurité", "SLA breach"],
        recommended_connectors=["ServiceNow", "Jira", "Datadog", "Splunk", "GitHub", "AWS/Azure/GCP"],
        compliance_notes=["NIS2", "ISO 27001", "SOC2", "least privilege"],
    ),
    "mechanical_industry": SectorPack(
        key="mechanical_industry",
        name="Mécanique / Manufacturing",
        typical_systems=["MES", "ERP", "PLM", "SCADA", "Quality", "Supply chain"],
        core_entities=["Product", "Machine", "Supplier", "Batch", "Incident", "QualityDefect", "Transaction"],
        anomaly_examples=["défaut qualité", "goulot production", "retard fournisseur", "coût matière", "panne machine"],
        recommended_connectors=["SAP", "Siemens Teamcenter", "OPC-UA", "MES", "QMS"],
        compliance_notes=["traçabilité lot", "qualité", "sécurité industrielle"],
    ),
    "public_sector": SectorPack(
        key="public_sector",
        name="Secteur public / Collectivités",
        typical_systems=["Case management", "Finance", "HR", "GIS", "Document management", "Citizen portal"],
        core_entities=["Citizen", "Case", "Department", "Contract", "Asset", "Document", "Risk"],
        anomaly_examples=["retard dossier", "risque budgétaire", "qualité service", "fraude", "incident infrastructure"],
        recommended_connectors=["SharePoint", "GIS", "ERP public", "CRM citizen", "Open data"],
        compliance_notes=["souveraineté", "accessibilité", "archivage", "GDPR"],
    ),
}
