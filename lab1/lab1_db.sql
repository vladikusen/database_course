PGDMP                         z           lab1    14.5    14.5 %    "           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            #           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            $           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            %           1262    16394    lab1    DATABASE     d   CREATE DATABASE lab1 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Ukrainian_Ukraine.1251';
    DROP DATABASE lab1;
                postgres    false            ?            1259    16566    car    TABLE     ?   CREATE TABLE public.car (
    car_vin text NOT NULL,
    car_brand text,
    car_type text,
    car_registration text NOT NULL
);
    DROP TABLE public.car;
       public         heap    postgres    false            ?            1259    16611    engine    TABLE     ?   CREATE TABLE public.engine (
    engine_code text NOT NULL,
    engine_vin text NOT NULL,
    engine_volume double precision,
    engine_type text,
    engine_power integer
);
    DROP TABLE public.engine;
       public         heap    postgres    false            ?            1259    16579    gas_station    TABLE     |   CREATE TABLE public.gas_station (
    gas_station_id integer NOT NULL,
    gas_station_name text,
    gas_station bit(1)
);
    DROP TABLE public.gas_station;
       public         heap    postgres    false            ?            1259    16594    gas_station_car    TABLE     ?   CREATE TABLE public.gas_station_car (
    gas_station_id integer NOT NULL,
    car_vin text NOT NULL,
    by_whom text,
    fuel_type text,
    amount_of_fuel integer
);
 #   DROP TABLE public.gas_station_car;
       public         heap    postgres    false            ?            1259    16578    gas_station_gas_station_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.gas_station_gas_station_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 5   DROP SEQUENCE public.gas_station_gas_station_id_seq;
       public          postgres    false    213            &           0    0    gas_station_gas_station_id_seq    SEQUENCE OWNED BY     a   ALTER SEQUENCE public.gas_station_gas_station_id_seq OWNED BY public.gas_station.gas_station_id;
          public          postgres    false    212            ?            1259    16545    owner    TABLE     u   CREATE TABLE public.owner (
    owner_car_registration text NOT NULL,
    owner_name text,
    owner_license text
);
    DROP TABLE public.owner;
       public         heap    postgres    false            ?            1259    16554    owner_license    TABLE     e   CREATE TABLE public.owner_license (
    owner_license text NOT NULL,
    owner_experience integer
);
 !   DROP TABLE public.owner_license;
       public         heap    postgres    false            ?            1259    16625    technical_inspection    TABLE     ?   CREATE TABLE public.technical_inspection (
    client_car_vin text NOT NULL,
    inspection_date date,
    inspection_result text
);
 (   DROP TABLE public.technical_inspection;
       public         heap    postgres    false            t           2604    16582    gas_station gas_station_id    DEFAULT     ?   ALTER TABLE ONLY public.gas_station ALTER COLUMN gas_station_id SET DEFAULT nextval('public.gas_station_gas_station_id_seq'::regclass);
 I   ALTER TABLE public.gas_station ALTER COLUMN gas_station_id DROP DEFAULT;
       public          postgres    false    212    213    213                      0    16566    car 
   TABLE DATA           M   COPY public.car (car_vin, car_brand, car_type, car_registration) FROM stdin;
    public          postgres    false    211   ?,                 0    16611    engine 
   TABLE DATA           c   COPY public.engine (engine_code, engine_vin, engine_volume, engine_type, engine_power) FROM stdin;
    public          postgres    false    215   ?,                 0    16579    gas_station 
   TABLE DATA           T   COPY public.gas_station (gas_station_id, gas_station_name, gas_station) FROM stdin;
    public          postgres    false    213   ?,                 0    16594    gas_station_car 
   TABLE DATA           f   COPY public.gas_station_car (gas_station_id, car_vin, by_whom, fuel_type, amount_of_fuel) FROM stdin;
    public          postgres    false    214   -                 0    16545    owner 
   TABLE DATA           R   COPY public.owner (owner_car_registration, owner_name, owner_license) FROM stdin;
    public          postgres    false    209   6-                 0    16554    owner_license 
   TABLE DATA           H   COPY public.owner_license (owner_license, owner_experience) FROM stdin;
    public          postgres    false    210   b-                 0    16625    technical_inspection 
   TABLE DATA           b   COPY public.technical_inspection (client_car_vin, inspection_date, inspection_result) FROM stdin;
    public          postgres    false    216   ?-       '           0    0    gas_station_gas_station_id_seq    SEQUENCE SET     M   SELECT pg_catalog.setval('public.gas_station_gas_station_id_seq', 1, false);
          public          postgres    false    212            |           2606    16572    car car_pkey 
   CONSTRAINT     O   ALTER TABLE ONLY public.car
    ADD CONSTRAINT car_pkey PRIMARY KEY (car_vin);
 6   ALTER TABLE ONLY public.car DROP CONSTRAINT car_pkey;
       public            postgres    false    211            ?           2606    16619    engine engine_engine_vin_key 
   CONSTRAINT     ]   ALTER TABLE ONLY public.engine
    ADD CONSTRAINT engine_engine_vin_key UNIQUE (engine_vin);
 F   ALTER TABLE ONLY public.engine DROP CONSTRAINT engine_engine_vin_key;
       public            postgres    false    215            ?           2606    16617    engine engine_pk 
   CONSTRAINT     c   ALTER TABLE ONLY public.engine
    ADD CONSTRAINT engine_pk PRIMARY KEY (engine_code, engine_vin);
 :   ALTER TABLE ONLY public.engine DROP CONSTRAINT engine_pk;
       public            postgres    false    215    215            ?           2606    16600 !   gas_station_car gas_station_carpk 
   CONSTRAINT     t   ALTER TABLE ONLY public.gas_station_car
    ADD CONSTRAINT gas_station_carpk PRIMARY KEY (car_vin, gas_station_id);
 K   ALTER TABLE ONLY public.gas_station_car DROP CONSTRAINT gas_station_carpk;
       public            postgres    false    214    214            ~           2606    16586    gas_station gas_station_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.gas_station
    ADD CONSTRAINT gas_station_pkey PRIMARY KEY (gas_station_id);
 F   ALTER TABLE ONLY public.gas_station DROP CONSTRAINT gas_station_pkey;
       public            postgres    false    213            z           2606    16560     owner_license owner_license_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.owner_license
    ADD CONSTRAINT owner_license_pkey PRIMARY KEY (owner_license);
 J   ALTER TABLE ONLY public.owner_license DROP CONSTRAINT owner_license_pkey;
       public            postgres    false    210            v           2606    16553    owner owner_owner_license_key 
   CONSTRAINT     a   ALTER TABLE ONLY public.owner
    ADD CONSTRAINT owner_owner_license_key UNIQUE (owner_license);
 G   ALTER TABLE ONLY public.owner DROP CONSTRAINT owner_owner_license_key;
       public            postgres    false    209            x           2606    16551    owner owner_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.owner
    ADD CONSTRAINT owner_pkey PRIMARY KEY (owner_car_registration);
 :   ALTER TABLE ONLY public.owner DROP CONSTRAINT owner_pkey;
       public            postgres    false    209            ?           2606    16631 .   technical_inspection technical_inspection_pkey 
   CONSTRAINT     x   ALTER TABLE ONLY public.technical_inspection
    ADD CONSTRAINT technical_inspection_pkey PRIMARY KEY (client_car_vin);
 X   ALTER TABLE ONLY public.technical_inspection DROP CONSTRAINT technical_inspection_pkey;
       public            postgres    false    216            ?           2606    16573    car car_car_registration_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.car
    ADD CONSTRAINT car_car_registration_fkey FOREIGN KEY (car_registration) REFERENCES public.owner(owner_car_registration);
 G   ALTER TABLE ONLY public.car DROP CONSTRAINT car_car_registration_fkey;
       public          postgres    false    209    211    3192            ?           2606    16620    engine engine_engine_vin_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.engine
    ADD CONSTRAINT engine_engine_vin_fkey FOREIGN KEY (engine_vin) REFERENCES public.car(car_vin);
 G   ALTER TABLE ONLY public.engine DROP CONSTRAINT engine_engine_vin_fkey;
       public          postgres    false    215    3196    211            ?           2606    16606 ,   gas_station_car gas_station_car_car_vin_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.gas_station_car
    ADD CONSTRAINT gas_station_car_car_vin_fkey FOREIGN KEY (car_vin) REFERENCES public.car(car_vin);
 V   ALTER TABLE ONLY public.gas_station_car DROP CONSTRAINT gas_station_car_car_vin_fkey;
       public          postgres    false    214    3196    211            ?           2606    16601 3   gas_station_car gas_station_car_gas_station_id_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.gas_station_car
    ADD CONSTRAINT gas_station_car_gas_station_id_fkey FOREIGN KEY (gas_station_id) REFERENCES public.gas_station(gas_station_id);
 ]   ALTER TABLE ONLY public.gas_station_car DROP CONSTRAINT gas_station_car_gas_station_id_fkey;
       public          postgres    false    214    3198    213            ?           2606    16561 .   owner_license owner_license_owner_license_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.owner_license
    ADD CONSTRAINT owner_license_owner_license_fkey FOREIGN KEY (owner_license) REFERENCES public.owner(owner_license);
 X   ALTER TABLE ONLY public.owner_license DROP CONSTRAINT owner_license_owner_license_fkey;
       public          postgres    false    209    210    3190            ?           2606    16632 =   technical_inspection technical_inspection_client_car_vin_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.technical_inspection
    ADD CONSTRAINT technical_inspection_client_car_vin_fkey FOREIGN KEY (client_car_vin) REFERENCES public.car(car_vin);
 g   ALTER TABLE ONLY public.technical_inspection DROP CONSTRAINT technical_inspection_client_car_vin_fkey;
       public          postgres    false    211    3196    216               +   x???,).M?,????????8?SS?8?2??K??b???? l?         /   x?3I7????,).M?,?????4?3??????K?440?????? ?N
?            x?????? ? ?            x?????? ? ?            x?K?,*.	?tQ?i ҇+F??? s??            x?K?,*.??4?????? !b            x?????? ? ?     