MERGE (org:Organization {id: 'demo-org', name: 'Demo Enterprise'})
MERGE (dept:Department {id: 'ops', name: 'Operations'})
MERGE (product:Product {id: 'product-a', name: 'Product A'})
MERGE (supplier:Supplier {id: 'supplier-acme', name: 'Supplier ACME'})
MERGE (incident:Incident {id: 'incident-line-3', name: 'Production delay line 3'})
MERGE (org)-[:CONTAINS]->(dept)
MERGE (dept)-[:OWNS]->(product)
MERGE (supplier)-[:SUPPLIES]->(product)
MERGE (incident)-[:IMPACTS]->(product);
