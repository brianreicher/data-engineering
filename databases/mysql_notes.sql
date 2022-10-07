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