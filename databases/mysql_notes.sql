-- display different local databases
show databases;

-- create arbitrary database
create database foo;

-- use bio database
use bio;

-- show tables in bio database
show tables;

SELECT *
FROM GAD;

select distinct gene_symbol
from gene;

SELECT phenotype, gene_symbol, count(*) as NumPubs
FROM gad
WHERE association = 'Y' and phenotype = 'asthma'
GROUP BY phenotype, gene_symbol
HAVING count(*)>=3
order by NumPubs desc;

SELECT *
FROM gene
WHERE gene_symbol = 'APOE';

SELECT *
FROM go
WHERE gene_id = (SELECT gene.gene_id
FROM gene
WHERE gene_symbol = 'APOE');


SELECT lower(phenotype) as phenotype, gene_symbol, count(*) as npubs
FROM gad
WHERE association = 'Y'
GROUP BY phenotype, gene_symbol
HAVING npubs>=3
ORDER BY npubs DESC;


# creating a view
CREATE VIEW  gad_clean as
SELECT association, lower(regexp_replace(phenotype, '[^a-zA-Z0-9] ', '')) as phenotype,
       disease_class, gene_symbol, pubmed_id
FROM gad
WHERE association = 'Y' and phenotype <> ''
ORDER BY phenotype, gene_symbol;

# referencing a view
CREATE VIEW gad_pubs as
SELECT phenotype, gene_symbol, count(*) as npubs
FROM gad_clean
GROUP BY phenotype, gene_symbol
ORDER BY phenotype, npubs DESC;

SELECT *
FROM gad_pubs
WHERE phenotype='asthma';


# sankey cleaning query -- much much shorter
SELECT *
FROM gad_pubs
WHERE gene_symbol in (
    SELECT gene_symbol
    FROM gad_pubs
    WHERE phenotype='asthma')
ORDER BY gene_symbol;
