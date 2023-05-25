PGDMP         :                {            APP3    14.7    14.7 >    3           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            4           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            5           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            6           1262    16931    APP3    DATABASE     b   CREATE DATABASE "APP3" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Spanish_Spain.1252';
    DROP DATABASE "APP3";
                postgres    false            �            1259    16940    admin    TABLE     V   CREATE TABLE public.admin (
    idad smallint NOT NULL,
    idus smallint NOT NULL
);
    DROP TABLE public.admin;
       public         heap    postgres    false            �            1259    16939    admin_idad_seq    SEQUENCE     �   CREATE SEQUENCE public.admin_idad_seq
    AS smallint
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.admin_idad_seq;
       public          postgres    false    212            7           0    0    admin_idad_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.admin_idad_seq OWNED BY public.admin.idad;
          public          postgres    false    211            �            1259    16978 
   comentario    TABLE     �   CREATE TABLE public.comentario (
    idc smallint NOT NULL,
    idus smallint NOT NULL,
    idcoms smallint,
    comentario character varying(100) NOT NULL,
    idp smallint NOT NULL
);
    DROP TABLE public.comentario;
       public         heap    postgres    false            �            1259    16977    comentario_idc_seq    SEQUENCE     �   CREATE SEQUENCE public.comentario_idc_seq
    AS smallint
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.comentario_idc_seq;
       public          postgres    false    218            8           0    0    comentario_idc_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.comentario_idc_seq OWNED BY public.comentario.idc;
          public          postgres    false    217            �            1259    16952    perfil    TABLE     W   CREATE TABLE public.perfil (
    idp smallint NOT NULL,
    public boolean NOT NULL
);
    DROP TABLE public.perfil;
       public         heap    postgres    false            �            1259    16951    perfil_idp_seq    SEQUENCE     �   CREATE SEQUENCE public.perfil_idp_seq
    AS smallint
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.perfil_idp_seq;
       public          postgres    false    214            9           0    0    perfil_idp_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.perfil_idp_seq OWNED BY public.perfil.idp;
          public          postgres    false    213            �            1259    16964    publicacion    TABLE     {  CREATE TABLE public.publicacion (
    idpc smallint NOT NULL,
    idus smallint NOT NULL,
    titulo character varying(15) NOT NULL,
    imagen bytea NOT NULL,
    descrip character varying(250) NOT NULL,
    precio character varying(6) NOT NULL,
    comida boolean,
    electronico boolean,
    libro boolean,
    accesorios boolean,
    papeleria boolean,
    dispo boolean
);
    DROP TABLE public.publicacion;
       public         heap    postgres    false            �            1259    16963    publicacion_idpc_seq    SEQUENCE     �   CREATE SEQUENCE public.publicacion_idpc_seq
    AS smallint
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.publicacion_idpc_seq;
       public          postgres    false    216            :           0    0    publicacion_idpc_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.publicacion_idpc_seq OWNED BY public.publicacion.idpc;
          public          postgres    false    215            �            1259    17000    reporte    TABLE     �   CREATE TABLE public.reporte (
    idr smallint NOT NULL,
    idp smallint NOT NULL,
    tipo boolean,
    comentario character varying(100) NOT NULL
);
    DROP TABLE public.reporte;
       public         heap    postgres    false            �            1259    16999    reporte_idr_seq    SEQUENCE     �   CREATE SEQUENCE public.reporte_idr_seq
    AS smallint
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.reporte_idr_seq;
       public          postgres    false    220            ;           0    0    reporte_idr_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.reporte_idr_seq OWNED BY public.reporte.idr;
          public          postgres    false    219            �            1259    16933    usuario    TABLE     �   CREATE TABLE public.usuario (
    id smallint NOT NULL,
    nombre character varying(15) NOT NULL,
    codigo character(9) NOT NULL,
    correo character varying(50) NOT NULL,
    contrasena character varying(15) NOT NULL
);
    DROP TABLE public.usuario;
       public         heap    postgres    false            �            1259    16932    usuario_id_seq    SEQUENCE     �   CREATE SEQUENCE public.usuario_id_seq
    AS smallint
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.usuario_id_seq;
       public          postgres    false    210            <           0    0    usuario_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.usuario_id_seq OWNED BY public.usuario.id;
          public          postgres    false    209            �            1259    17012    venta    TABLE     �   CREATE TABLE public.venta (
    idv smallint NOT NULL,
    idus smallint NOT NULL,
    idpb smallint NOT NULL,
    fecha date NOT NULL
);
    DROP TABLE public.venta;
       public         heap    postgres    false            �            1259    17011    venta_idv_seq    SEQUENCE     �   CREATE SEQUENCE public.venta_idv_seq
    AS smallint
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.venta_idv_seq;
       public          postgres    false    222            =           0    0    venta_idv_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.venta_idv_seq OWNED BY public.venta.idv;
          public          postgres    false    221            {           2604    16943 
   admin idad    DEFAULT     h   ALTER TABLE ONLY public.admin ALTER COLUMN idad SET DEFAULT nextval('public.admin_idad_seq'::regclass);
 9   ALTER TABLE public.admin ALTER COLUMN idad DROP DEFAULT;
       public          postgres    false    212    211    212            ~           2604    16981    comentario idc    DEFAULT     p   ALTER TABLE ONLY public.comentario ALTER COLUMN idc SET DEFAULT nextval('public.comentario_idc_seq'::regclass);
 =   ALTER TABLE public.comentario ALTER COLUMN idc DROP DEFAULT;
       public          postgres    false    217    218    218            |           2604    16955 
   perfil idp    DEFAULT     h   ALTER TABLE ONLY public.perfil ALTER COLUMN idp SET DEFAULT nextval('public.perfil_idp_seq'::regclass);
 9   ALTER TABLE public.perfil ALTER COLUMN idp DROP DEFAULT;
       public          postgres    false    213    214    214            }           2604    16967    publicacion idpc    DEFAULT     t   ALTER TABLE ONLY public.publicacion ALTER COLUMN idpc SET DEFAULT nextval('public.publicacion_idpc_seq'::regclass);
 ?   ALTER TABLE public.publicacion ALTER COLUMN idpc DROP DEFAULT;
       public          postgres    false    216    215    216                       2604    17003    reporte idr    DEFAULT     j   ALTER TABLE ONLY public.reporte ALTER COLUMN idr SET DEFAULT nextval('public.reporte_idr_seq'::regclass);
 :   ALTER TABLE public.reporte ALTER COLUMN idr DROP DEFAULT;
       public          postgres    false    220    219    220            z           2604    16936 
   usuario id    DEFAULT     h   ALTER TABLE ONLY public.usuario ALTER COLUMN id SET DEFAULT nextval('public.usuario_id_seq'::regclass);
 9   ALTER TABLE public.usuario ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    209    210    210            �           2604    17015 	   venta idv    DEFAULT     f   ALTER TABLE ONLY public.venta ALTER COLUMN idv SET DEFAULT nextval('public.venta_idv_seq'::regclass);
 8   ALTER TABLE public.venta ALTER COLUMN idv DROP DEFAULT;
       public          postgres    false    221    222    222            &          0    16940    admin 
   TABLE DATA           +   COPY public.admin (idad, idus) FROM stdin;
    public          postgres    false    212   �D       ,          0    16978 
   comentario 
   TABLE DATA           H   COPY public.comentario (idc, idus, idcoms, comentario, idp) FROM stdin;
    public          postgres    false    218   �D       (          0    16952    perfil 
   TABLE DATA           -   COPY public.perfil (idp, public) FROM stdin;
    public          postgres    false    214   E       *          0    16964    publicacion 
   TABLE DATA           �   COPY public.publicacion (idpc, idus, titulo, imagen, descrip, precio, comida, electronico, libro, accesorios, papeleria, dispo) FROM stdin;
    public          postgres    false    216   +E       .          0    17000    reporte 
   TABLE DATA           =   COPY public.reporte (idr, idp, tipo, comentario) FROM stdin;
    public          postgres    false    220   HE       $          0    16933    usuario 
   TABLE DATA           I   COPY public.usuario (id, nombre, codigo, correo, contrasena) FROM stdin;
    public          postgres    false    210   eE       0          0    17012    venta 
   TABLE DATA           7   COPY public.venta (idv, idus, idpb, fecha) FROM stdin;
    public          postgres    false    222   �E       >           0    0    admin_idad_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.admin_idad_seq', 1, false);
          public          postgres    false    211            ?           0    0    comentario_idc_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.comentario_idc_seq', 1, false);
          public          postgres    false    217            @           0    0    perfil_idp_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.perfil_idp_seq', 1, false);
          public          postgres    false    213            A           0    0    publicacion_idpc_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.publicacion_idpc_seq', 1, false);
          public          postgres    false    215            B           0    0    reporte_idr_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.reporte_idr_seq', 1, false);
          public          postgres    false    219            C           0    0    usuario_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.usuario_id_seq', 1, false);
          public          postgres    false    209            D           0    0    venta_idv_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public.venta_idv_seq', 1, false);
          public          postgres    false    221            �           2606    16945    admin admin_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.admin
    ADD CONSTRAINT admin_pkey PRIMARY KEY (idad);
 :   ALTER TABLE ONLY public.admin DROP CONSTRAINT admin_pkey;
       public            postgres    false    212            �           2606    16983    comentario comentario_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public.comentario
    ADD CONSTRAINT comentario_pkey PRIMARY KEY (idc);
 D   ALTER TABLE ONLY public.comentario DROP CONSTRAINT comentario_pkey;
       public            postgres    false    218            �           2606    16957    perfil perfil_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.perfil
    ADD CONSTRAINT perfil_pkey PRIMARY KEY (idp);
 <   ALTER TABLE ONLY public.perfil DROP CONSTRAINT perfil_pkey;
       public            postgres    false    214            �           2606    16971    publicacion publicacion_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.publicacion
    ADD CONSTRAINT publicacion_pkey PRIMARY KEY (idpc);
 F   ALTER TABLE ONLY public.publicacion DROP CONSTRAINT publicacion_pkey;
       public            postgres    false    216            �           2606    17005    reporte reporte_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.reporte
    ADD CONSTRAINT reporte_pkey PRIMARY KEY (idr);
 >   ALTER TABLE ONLY public.reporte DROP CONSTRAINT reporte_pkey;
       public            postgres    false    220            �           2606    16938    usuario usuario_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.usuario DROP CONSTRAINT usuario_pkey;
       public            postgres    false    210            �           2606    17017    venta venta_pkey 
   CONSTRAINT     O   ALTER TABLE ONLY public.venta
    ADD CONSTRAINT venta_pkey PRIMARY KEY (idv);
 :   ALTER TABLE ONLY public.venta DROP CONSTRAINT venta_pkey;
       public            postgres    false    222            �           2606    16946    admin admin_idus_fkey    FK CONSTRAINT     s   ALTER TABLE ONLY public.admin
    ADD CONSTRAINT admin_idus_fkey FOREIGN KEY (idus) REFERENCES public.usuario(id);
 ?   ALTER TABLE ONLY public.admin DROP CONSTRAINT admin_idus_fkey;
       public          postgres    false    210    3202    212            �           2606    16994 !   comentario comentario_idcoms_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.comentario
    ADD CONSTRAINT comentario_idcoms_fkey FOREIGN KEY (idcoms) REFERENCES public.comentario(idc);
 K   ALTER TABLE ONLY public.comentario DROP CONSTRAINT comentario_idcoms_fkey;
       public          postgres    false    218    3210    218            �           2606    16984    comentario comentario_idp_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.comentario
    ADD CONSTRAINT comentario_idp_fkey FOREIGN KEY (idp) REFERENCES public.publicacion(idpc);
 H   ALTER TABLE ONLY public.comentario DROP CONSTRAINT comentario_idp_fkey;
       public          postgres    false    3208    218    216            �           2606    16989    comentario comentario_idus_fkey    FK CONSTRAINT     }   ALTER TABLE ONLY public.comentario
    ADD CONSTRAINT comentario_idus_fkey FOREIGN KEY (idus) REFERENCES public.usuario(id);
 I   ALTER TABLE ONLY public.comentario DROP CONSTRAINT comentario_idus_fkey;
       public          postgres    false    218    210    3202            �           2606    16958    perfil perfil_idp_fkey    FK CONSTRAINT     s   ALTER TABLE ONLY public.perfil
    ADD CONSTRAINT perfil_idp_fkey FOREIGN KEY (idp) REFERENCES public.usuario(id);
 @   ALTER TABLE ONLY public.perfil DROP CONSTRAINT perfil_idp_fkey;
       public          postgres    false    214    3202    210            �           2606    16972 !   publicacion publicacion_idus_fkey    FK CONSTRAINT        ALTER TABLE ONLY public.publicacion
    ADD CONSTRAINT publicacion_idus_fkey FOREIGN KEY (idus) REFERENCES public.usuario(id);
 K   ALTER TABLE ONLY public.publicacion DROP CONSTRAINT publicacion_idus_fkey;
       public          postgres    false    216    3202    210            �           2606    17006    reporte reporte_idp_fkey    FK CONSTRAINT     {   ALTER TABLE ONLY public.reporte
    ADD CONSTRAINT reporte_idp_fkey FOREIGN KEY (idp) REFERENCES public.publicacion(idpc);
 B   ALTER TABLE ONLY public.reporte DROP CONSTRAINT reporte_idp_fkey;
       public          postgres    false    3208    220    216            �           2606    17018    venta venta_idus_fkey    FK CONSTRAINT     y   ALTER TABLE ONLY public.venta
    ADD CONSTRAINT venta_idus_fkey FOREIGN KEY (idus) REFERENCES public.publicacion(idpc);
 ?   ALTER TABLE ONLY public.venta DROP CONSTRAINT venta_idus_fkey;
       public          postgres    false    216    3208    222            �           2606    17023    venta venta_idus_fkey1    FK CONSTRAINT     t   ALTER TABLE ONLY public.venta
    ADD CONSTRAINT venta_idus_fkey1 FOREIGN KEY (idus) REFERENCES public.usuario(id);
 @   ALTER TABLE ONLY public.venta DROP CONSTRAINT venta_idus_fkey1;
       public          postgres    false    210    3202    222            &      x������ � �      ,      x������ � �      (      x������ � �      *      x������ � �      .      x������ � �      $      x������ � �      0      x������ � �     