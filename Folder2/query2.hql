SET hive.exec.dynamic.partition=true;

SET hive.exec.dynamic.partition.mode=nonstrict;

REFRESH TABLE data_lake_analytics.tmp_abnpaychannel{{ envCode }};

insert overwrite table data_lake_analytics.STG_ABNpagos_m{{ envCode }} partition(periodo, flag_fan)

SELECT

    NVL(pri_identity, c.linea) as linea,

    payment_method_id,

    bank_code,

    p.medio_pago,

    cp.description as tipo_pago,

    p.canal_pago,

    (p.payment_amt/1000000) as importe,

    cast(PAYMENT_DATE as int) as fecha,

    cast(substr(PAYMENT_DATE,1,6) as int) AS periodo,

    1 as flag_fan

from data_lake_analytics.tmp_abnpagosfan{{ envCode }} p

 

left join (select contrato_key, linea, cbs_cust_id

            from data_lake_analytics.STG_ABNparque_m{{ envCode }}

            where periodo = from_unixtime(unix_timestamp(date_add(cast('{{ next_ds }}' as date),-day(cast('{{ next_ds }}' as date))),'yyyy-MM-dd'), 'yyyyMM')

    ) c

    on c.cbs_cust_id = p.cust_id

 

left join data_lake_analytics.tmp_abnpaychannel{{ envCode }} cp

    on cp.channel_id = p.channel_id

where substr(PAYMENT_DATE,1,6) = from_unixtime(unix_timestamp(date_add(cast('{{ next_ds }}' as date),-day(cast('{{ next_ds }}' as date))),'yyyy-MM-dd'), 'yyyyMM')

;

 

REFRESH TABLE data_lake_analytics.STG_ABNpagos_m{{ envCode }};