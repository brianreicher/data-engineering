-- display different local databases
show databases;

-- create aribitray database
create database foo;

-- use bio database
use bio;

-- show tables in bio database
show tables;

SELECT *
FROM GAD;

select distinct gene_symbol
from gene;

SELECT phenotype, gene_symbol
FROM gad
WHERE association = 'Y' and phenotype = 'asthma'
GROUP BY phenotype, gene_symbol
order by phenotype, gene_symbol;