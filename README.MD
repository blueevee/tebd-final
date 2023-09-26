# TEBD ATIVIDADE DO SEMESTRE

## PRÓXIMOS PASSOS
> - Criação do DATAWAREHOUSE com todos os dados:
>> - **Tratar os dados:**
>> - 4.a – Quantos registros de AIH existem para cada mês e em cada estado?
>> - 4.b – Quantos registros de Procedimentos de Saúde foram importados?
>> - 4.c – Quantos registros de CID foram importados?

>> - **Criar tabelas:**
>> - INTERNAMENTOS (SIH 2019 - 2022)
>> - PROCEDIMENTOS (tratamentos resgistrados)
>> - CID (enfermidades registradas)
>> - ESTABELECIMENTOS (CNES + MUNICIPIOS)

### Instruções do trabalho:
3. Depois a conversão de todos os arquivos para .CSV é necessário gerar um banco de dados para que estes arquivos sejam importados. Este banco de dados representa os “dados brutos”. Ou seja, não se trata de um banco de dados relacional. Trata-se apenas da fonte original de dados para as próximas etapas do projeto.

O banco de dados a ser gerado é de livre escolha (Sql Server, SQL Express, MySql ou outros).

4. Para efeito de registro e checagem das informações iniciais alguns levantamentos devem ser feitos:

4.a – Quantos registros de AIH existem para cada mês e em cada estado?

4.b – Quantos registros de Procedimentos de Saúde foram importados?

4.c – Quantos registros de CID foram importados?

#### Etapa 02 – Modelagem do DW

Nesta etapa devemos criar uma nova base de dados com a modelagem dimensional para medir os indicadores que desejamos. Nesta etapa deve-se pensar como devemos estruturar as tabelas fato e dimensão.

Segue abaixo alguns indicadores interessantes para serem considerados:

1 – Quantidade de AIHs por: Estado, Município, CNES, Ano, Mês, Procedimento, CID.

2 – Valores pagos por: Estado, Município, CNES, Ano, Mês, Procedimento, CID

3 – Tempo de permanência de internação nas mesmas dimensões.

Na etapa anterior tratamos de parte do processo de ETL (Extract Transform Load) que compreendemos a extração/coleta dos dados. Agora teremos que trabalhar na transformação e carga dos dados para a base de dados onde modelamos o DW.

Devemos verificar com atenção os quantitativos levantados no item 4 da Etapa 01, pois agora teremos que alimentar novas tabelas com chaves e índices que estão relacionadas. Neste momento, a carga de dados pode gerar algumas inconsistências.

#### Etapa 03 – Apresentação

Construção de um painel (ou mais) com indicadores críticos, que dê uma visão rápida da sua performance, capaz de aceitar algum tipo de interatividade com o utilizador e que seja fácil de atualizar.

A indicação é de uso do Power BI, mas podem utilizar outras ferramentas, contanto que esteja disponível no momento da apresentação e não limite a entrega.

Deve ser elaborado um relatório do trabalho com os dados analisados.

A equipe deve apresentar o Dashboard e suas análises numa aula síncrona e postar no repositório do Teams da turma o documento com o relatório do trabalho.

#### NOTAS
> Na tabela de municipios foi adicionada uma coluna topology que classifica se um municipio é rural/urbano para conseguir métricas como quantidades de estabelecimentos por tipo de área
> Legenda: 1-Urbano, 2-Intermediário Adjacente, 3-Intermediário Remoto, 4-Rural Adjacente, 5-Rural Remoto