USE master; -- USE master: seleciona o banco de sistema a partir do qual criaremos nosso banco.
GO -- GO: separa os blocos de comandos para execução no SSMS.

IF DB_ID(N'CruzeiroAnalytics') IS NULL -- IF DB_ID(...) IS NULL: verifica se o banco ainda não existe.
BEGIN 
    CREATE DATABASE [CruzeiroAnalytics]; -- CREATE DATABASE: cria o banco CruzeiroAnalytics. Se ele já existir, esse bloco será ignorado.
END;
GO