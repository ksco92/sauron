create schema if not exists sauron;

drop view if exists sauron.all_transactions;
drop function if exists sauron.get_capital_one_debit_transaction_id;
drop table if exists sauron.capital_one_debit;
drop table if exists sauron.sub_categories;
drop table if exists sauron.categories;

create table sauron.categories
(
    category_id   serial,
    category_name varchar(50),
    primary key (category_id)
);

create table sauron.sub_categories
(
    sub_category_id   serial,
    sub_category_name varchar(50),
    category_id       integer,
    primary key (sub_category_id),
    foreign key (category_id) references sauron.categories (category_id)
);

create table sauron.capital_one_debit
(
    transaction_id          uuid,
    account_number          integer        not null,
    transaction_date        date           not null,
    transaction_amount      numeric(18, 2) not null,
    transaction_type        varchar(6)     not null,
    transaction_description text           not null,
    balance                 numeric(18, 2) not null,
    sub_category_id         integer,
    primary key (transaction_id),
    foreign key (sub_category_id) references sauron.sub_categories (sub_category_id)
);

create or replace function sauron.get_capital_one_debit_transaction_id(
    account_number integer,
    transaction_date date,
    transaction_amount numeric(18, 2),
    transaction_type varchar(6),
    transaction_description text,
    balance numeric(18, 2))
    returns uuid
    language sql
    immutable as
'select md5(account_number::varchar ||
            transaction_date::varchar ||
            transaction_amount::varchar ||
            transaction_type ||
            transaction_description ||
            balance::varchar)::uuid';

create or replace view sauron.all_transactions as
select cod.transaction_date,
       cod.transaction_amount,
       cod.transaction_description,
       c.category_name,
       sc.sub_category_name
from sauron.capital_one_debit cod
         left join sauron.sub_categories sc
                   on cod.sub_category_id = sc.sub_category_id
         left join sauron.categories c
                   on sc.category_id = c.category_id;