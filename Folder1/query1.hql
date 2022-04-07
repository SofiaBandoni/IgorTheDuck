drop table if exists data_lake_analytics.tmp_abnbankinfo{{ envCode }} purge;

 

create external table data_lake_analytics.tmp_abnbankinfo{{ envCode }} as

select distinct bank_code,

    FIRST_value(bank_name) over(partition by bank_code order by day desc) as bank_name

from pre_facturacion.cbs_ar_dic_bank_info;