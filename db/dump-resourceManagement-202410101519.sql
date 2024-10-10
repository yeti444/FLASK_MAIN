--
-- PostgreSQL database dump
--

-- Dumped from database version 17.0
-- Dumped by pg_dump version 17.0

-- Started on 2024-10-10 15:19:03

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4963 (class 1262 OID 16384)
-- Name: resourceManagement; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE "resourceManagement" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.UTF-8';


ALTER DATABASE "resourceManagement" OWNER TO postgres;

\connect "resourceManagement"

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 5 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO postgres;

--
-- TOC entry 4964 (class 0 OID 0)
-- Dependencies: 5
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 217 (class 1259 OID 16385)
-- Name: maintanedresources; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.maintanedresources (
    maintid integer NOT NULL,
    resourceid integer NOT NULL
);


ALTER TABLE public.maintanedresources OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 16388)
-- Name: maintanedresources_maintid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.maintanedresources_maintid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.maintanedresources_maintid_seq OWNER TO postgres;

--
-- TOC entry 4965 (class 0 OID 0)
-- Dependencies: 218
-- Name: maintanedresources_maintid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.maintanedresources_maintid_seq OWNED BY public.maintanedresources.maintid;


--
-- TOC entry 219 (class 1259 OID 16389)
-- Name: maintanedresources_resourceid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.maintanedresources_resourceid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.maintanedresources_resourceid_seq OWNER TO postgres;

--
-- TOC entry 4966 (class 0 OID 0)
-- Dependencies: 219
-- Name: maintanedresources_resourceid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.maintanedresources_resourceid_seq OWNED BY public.maintanedresources.resourceid;


--
-- TOC entry 240 (class 1259 OID 16505)
-- Name: maintenancetype; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.maintenancetype (
    maintenancetypeid integer NOT NULL,
    typename character varying NOT NULL
);


ALTER TABLE public.maintenancetype OWNER TO postgres;

--
-- TOC entry 239 (class 1259 OID 16504)
-- Name: maintenancetype_maintenancetypeid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.maintenancetype_maintenancetypeid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.maintenancetype_maintenancetypeid_seq OWNER TO postgres;

--
-- TOC entry 4967 (class 0 OID 0)
-- Dependencies: 239
-- Name: maintenancetype_maintenancetypeid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.maintenancetype_maintenancetypeid_seq OWNED BY public.maintenancetype.maintenancetypeid;


--
-- TOC entry 220 (class 1259 OID 16390)
-- Name: resources; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.resources (
    resourceid integer NOT NULL,
    name character varying NOT NULL,
    typeid integer NOT NULL,
    info json NOT NULL,
    "createdDate" timestamp with time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.resources OWNER TO postgres;

--
-- TOC entry 4968 (class 0 OID 0)
-- Dependencies: 220
-- Name: TABLE resources; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public.resources IS 'Resources table stores the data about resources';


--
-- TOC entry 221 (class 1259 OID 16396)
-- Name: resources_resourceid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.resources_resourceid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.resources_resourceid_seq OWNER TO postgres;

--
-- TOC entry 4969 (class 0 OID 0)
-- Dependencies: 221
-- Name: resources_resourceid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.resources_resourceid_seq OWNED BY public.resources.resourceid;


--
-- TOC entry 222 (class 1259 OID 16397)
-- Name: resources_typeid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.resources_typeid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.resources_typeid_seq OWNER TO postgres;

--
-- TOC entry 4970 (class 0 OID 0)
-- Dependencies: 222
-- Name: resources_typeid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.resources_typeid_seq OWNED BY public.resources.typeid;


--
-- TOC entry 223 (class 1259 OID 16398)
-- Name: resourcetypes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.resourcetypes (
    typeid integer NOT NULL,
    typename character varying NOT NULL
);


ALTER TABLE public.resourcetypes OWNER TO postgres;

--
-- TOC entry 224 (class 1259 OID 16403)
-- Name: resourcetypes_typeid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.resourcetypes_typeid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.resourcetypes_typeid_seq OWNER TO postgres;

--
-- TOC entry 4971 (class 0 OID 0)
-- Dependencies: 224
-- Name: resourcetypes_typeid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.resourcetypes_typeid_seq OWNED BY public.resourcetypes.typeid;


--
-- TOC entry 225 (class 1259 OID 16404)
-- Name: scheduledmaintenance; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.scheduledmaintenance (
    maintid integer NOT NULL,
    userid integer NOT NULL,
    fromdate timestamp with time zone NOT NULL,
    duration interval NOT NULL,
    createdate timestamp with time zone DEFAULT now() NOT NULL,
    description text,
    maintenancetypeid integer NOT NULL
);


ALTER TABLE public.scheduledmaintenance OWNER TO postgres;

--
-- TOC entry 226 (class 1259 OID 16408)
-- Name: scheduledmaintenance_maintid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.scheduledmaintenance_maintid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.scheduledmaintenance_maintid_seq OWNER TO postgres;

--
-- TOC entry 4972 (class 0 OID 0)
-- Dependencies: 226
-- Name: scheduledmaintenance_maintid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.scheduledmaintenance_maintid_seq OWNED BY public.scheduledmaintenance.maintid;


--
-- TOC entry 227 (class 1259 OID 16409)
-- Name: scheduledmaintenance_userid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.scheduledmaintenance_userid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.scheduledmaintenance_userid_seq OWNER TO postgres;

--
-- TOC entry 4973 (class 0 OID 0)
-- Dependencies: 227
-- Name: scheduledmaintenance_userid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.scheduledmaintenance_userid_seq OWNED BY public.scheduledmaintenance.userid;


--
-- TOC entry 228 (class 1259 OID 16410)
-- Name: scheduledresources; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.scheduledresources (
    workid integer NOT NULL,
    resourceid integer NOT NULL
);


ALTER TABLE public.scheduledresources OWNER TO postgres;

--
-- TOC entry 229 (class 1259 OID 16413)
-- Name: scheduledresources_resourceid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.scheduledresources_resourceid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.scheduledresources_resourceid_seq OWNER TO postgres;

--
-- TOC entry 4974 (class 0 OID 0)
-- Dependencies: 229
-- Name: scheduledresources_resourceid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.scheduledresources_resourceid_seq OWNED BY public.scheduledresources.resourceid;


--
-- TOC entry 230 (class 1259 OID 16414)
-- Name: scheduledresources_workid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.scheduledresources_workid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.scheduledresources_workid_seq OWNER TO postgres;

--
-- TOC entry 4975 (class 0 OID 0)
-- Dependencies: 230
-- Name: scheduledresources_workid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.scheduledresources_workid_seq OWNED BY public.scheduledresources.workid;


--
-- TOC entry 231 (class 1259 OID 16415)
-- Name: scheduledwork; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.scheduledwork (
    workid integer NOT NULL,
    userid integer NOT NULL,
    fromdate timestamp with time zone NOT NULL,
    duration interval NOT NULL,
    createdate timestamp with time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.scheduledwork OWNER TO postgres;

--
-- TOC entry 232 (class 1259 OID 16419)
-- Name: scheduledwork_userid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.scheduledwork_userid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.scheduledwork_userid_seq OWNER TO postgres;

--
-- TOC entry 4976 (class 0 OID 0)
-- Dependencies: 232
-- Name: scheduledwork_userid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.scheduledwork_userid_seq OWNED BY public.scheduledwork.userid;


--
-- TOC entry 233 (class 1259 OID 16420)
-- Name: scheduledwork_workid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.scheduledwork_workid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.scheduledwork_workid_seq OWNER TO postgres;

--
-- TOC entry 4977 (class 0 OID 0)
-- Dependencies: 233
-- Name: scheduledwork_workid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.scheduledwork_workid_seq OWNED BY public.scheduledwork.workid;


--
-- TOC entry 234 (class 1259 OID 16421)
-- Name: userdata; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.userdata (
    userid integer NOT NULL,
    email character varying NOT NULL,
    firstname character varying NOT NULL,
    lastname character varying NOT NULL,
    password character varying NOT NULL,
    createdate timestamp with time zone DEFAULT now() NOT NULL,
    roleid integer NOT NULL
);


ALTER TABLE public.userdata OWNER TO postgres;

--
-- TOC entry 4978 (class 0 OID 0)
-- Dependencies: 234
-- Name: TABLE userdata; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public.userdata IS 'This is the userdata table, which stores the user data.';


--
-- TOC entry 235 (class 1259 OID 16427)
-- Name: userdata_roleid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.userdata_roleid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.userdata_roleid_seq OWNER TO postgres;

--
-- TOC entry 4979 (class 0 OID 0)
-- Dependencies: 235
-- Name: userdata_roleid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.userdata_roleid_seq OWNED BY public.userdata.roleid;


--
-- TOC entry 236 (class 1259 OID 16428)
-- Name: userdata_userid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.userdata_userid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.userdata_userid_seq OWNER TO postgres;

--
-- TOC entry 4980 (class 0 OID 0)
-- Dependencies: 236
-- Name: userdata_userid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.userdata_userid_seq OWNED BY public.userdata.userid;


--
-- TOC entry 237 (class 1259 OID 16429)
-- Name: userroles; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.userroles (
    roleid integer NOT NULL,
    rolename character varying NOT NULL
);


ALTER TABLE public.userroles OWNER TO postgres;

--
-- TOC entry 238 (class 1259 OID 16434)
-- Name: userroles_roleid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.userroles_roleid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.userroles_roleid_seq OWNER TO postgres;

--
-- TOC entry 4981 (class 0 OID 0)
-- Dependencies: 238
-- Name: userroles_roleid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.userroles_roleid_seq OWNED BY public.userroles.roleid;


--
-- TOC entry 4741 (class 2604 OID 16435)
-- Name: maintanedresources maintid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.maintanedresources ALTER COLUMN maintid SET DEFAULT nextval('public.maintanedresources_maintid_seq'::regclass);


--
-- TOC entry 4742 (class 2604 OID 16436)
-- Name: maintanedresources resourceid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.maintanedresources ALTER COLUMN resourceid SET DEFAULT nextval('public.maintanedresources_resourceid_seq'::regclass);


--
-- TOC entry 4759 (class 2604 OID 16508)
-- Name: maintenancetype maintenancetypeid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.maintenancetype ALTER COLUMN maintenancetypeid SET DEFAULT nextval('public.maintenancetype_maintenancetypeid_seq'::regclass);


--
-- TOC entry 4743 (class 2604 OID 16437)
-- Name: resources resourceid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resources ALTER COLUMN resourceid SET DEFAULT nextval('public.resources_resourceid_seq'::regclass);


--
-- TOC entry 4744 (class 2604 OID 16438)
-- Name: resources typeid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resources ALTER COLUMN typeid SET DEFAULT nextval('public.resources_typeid_seq'::regclass);


--
-- TOC entry 4746 (class 2604 OID 16439)
-- Name: resourcetypes typeid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resourcetypes ALTER COLUMN typeid SET DEFAULT nextval('public.resourcetypes_typeid_seq'::regclass);


--
-- TOC entry 4747 (class 2604 OID 16440)
-- Name: scheduledmaintenance maintid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scheduledmaintenance ALTER COLUMN maintid SET DEFAULT nextval('public.scheduledmaintenance_maintid_seq'::regclass);


--
-- TOC entry 4748 (class 2604 OID 16441)
-- Name: scheduledmaintenance userid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scheduledmaintenance ALTER COLUMN userid SET DEFAULT nextval('public.scheduledmaintenance_userid_seq'::regclass);


--
-- TOC entry 4750 (class 2604 OID 16442)
-- Name: scheduledresources workid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scheduledresources ALTER COLUMN workid SET DEFAULT nextval('public.scheduledresources_workid_seq'::regclass);


--
-- TOC entry 4751 (class 2604 OID 16443)
-- Name: scheduledresources resourceid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scheduledresources ALTER COLUMN resourceid SET DEFAULT nextval('public.scheduledresources_resourceid_seq'::regclass);


--
-- TOC entry 4752 (class 2604 OID 16444)
-- Name: scheduledwork workid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scheduledwork ALTER COLUMN workid SET DEFAULT nextval('public.scheduledwork_workid_seq'::regclass);


--
-- TOC entry 4753 (class 2604 OID 16445)
-- Name: scheduledwork userid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scheduledwork ALTER COLUMN userid SET DEFAULT nextval('public.scheduledwork_userid_seq'::regclass);


--
-- TOC entry 4755 (class 2604 OID 16446)
-- Name: userdata userid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.userdata ALTER COLUMN userid SET DEFAULT nextval('public.userdata_userid_seq'::regclass);


--
-- TOC entry 4757 (class 2604 OID 16447)
-- Name: userdata roleid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.userdata ALTER COLUMN roleid SET DEFAULT nextval('public.userdata_roleid_seq'::regclass);


--
-- TOC entry 4758 (class 2604 OID 16448)
-- Name: userroles roleid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.userroles ALTER COLUMN roleid SET DEFAULT nextval('public.userroles_roleid_seq'::regclass);


--
-- TOC entry 4934 (class 0 OID 16385)
-- Dependencies: 217
-- Data for Name: maintanedresources; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.maintanedresources VALUES (1, 1);
INSERT INTO public.maintanedresources VALUES (2, 1);
INSERT INTO public.maintanedresources VALUES (3, 1);


--
-- TOC entry 4957 (class 0 OID 16505)
-- Dependencies: 240
-- Data for Name: maintenancetype; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.maintenancetype VALUES (1, 'Common');


--
-- TOC entry 4937 (class 0 OID 16390)
-- Dependencies: 220
-- Data for Name: resources; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.resources VALUES (1, 'test', 1, '{"x":100, "y":300, "z":400}', '2024-09-20 14:48:39.738442+02');


--
-- TOC entry 4940 (class 0 OID 16398)
-- Dependencies: 223
-- Data for Name: resourcetypes; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.resourcetypes VALUES (1, 'Nyomtato');


--
-- TOC entry 4942 (class 0 OID 16404)
-- Dependencies: 225
-- Data for Name: scheduledmaintenance; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.scheduledmaintenance VALUES (2, 1, '2025-01-01 00:00:00+01', '24:00:00', '2024-10-05 14:53:01.934511+02', 'test', 1);
INSERT INTO public.scheduledmaintenance VALUES (3, 1, '2025-01-01 00:00:00+01', '24:00:00', '2024-10-05 14:53:15.065872+02', 'test', 1);
INSERT INTO public.scheduledmaintenance VALUES (1, 1, '2024-10-08 00:00:00+02', '12:00:00', '2024-10-05 14:26:13.057084+02', 'Test', 1);


--
-- TOC entry 4945 (class 0 OID 16410)
-- Dependencies: 228
-- Data for Name: scheduledresources; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.scheduledresources VALUES (2, 1);
INSERT INTO public.scheduledresources VALUES (1, 1);


--
-- TOC entry 4948 (class 0 OID 16415)
-- Dependencies: 231
-- Data for Name: scheduledwork; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.scheduledwork VALUES (2, 1, '2024-11-01 00:00:00+01', '00:24:00', '2024-10-05 14:04:21.265003+02');
INSERT INTO public.scheduledwork VALUES (3, 1, '2024-12-01 00:00:00+01', '24:00:00', '2024-10-05 14:05:27.283368+02');
INSERT INTO public.scheduledwork VALUES (1, 1, '2024-10-05 00:00:00+02', '00:12:00', '2024-10-05 13:38:09.936184+02');


--
-- TOC entry 4951 (class 0 OID 16421)
-- Dependencies: 234
-- Data for Name: userdata; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.userdata VALUES (1, 'kristof20011020@gmail.com', 'Kristof Mark', 'Jakab', 'password', '2024-09-20 13:04:21.761875+02', 1);
INSERT INTO public.userdata VALUES (4, 'yeti4441@gmail.com', 'Random', 'Random', 'password', '2024-10-03 10:29:52.586565+02', 1);


--
-- TOC entry 4954 (class 0 OID 16429)
-- Dependencies: 237
-- Data for Name: userroles; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.userroles VALUES (1, 'Admin');


--
-- TOC entry 4982 (class 0 OID 0)
-- Dependencies: 218
-- Name: maintanedresources_maintid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.maintanedresources_maintid_seq', 1, false);


--
-- TOC entry 4983 (class 0 OID 0)
-- Dependencies: 219
-- Name: maintanedresources_resourceid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.maintanedresources_resourceid_seq', 1, false);


--
-- TOC entry 4984 (class 0 OID 0)
-- Dependencies: 239
-- Name: maintenancetype_maintenancetypeid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.maintenancetype_maintenancetypeid_seq', 1, true);


--
-- TOC entry 4985 (class 0 OID 0)
-- Dependencies: 221
-- Name: resources_resourceid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.resources_resourceid_seq', 195, true);


--
-- TOC entry 4986 (class 0 OID 0)
-- Dependencies: 222
-- Name: resources_typeid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.resources_typeid_seq', 1, false);


--
-- TOC entry 4987 (class 0 OID 0)
-- Dependencies: 224
-- Name: resourcetypes_typeid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.resourcetypes_typeid_seq', 111, true);


--
-- TOC entry 4988 (class 0 OID 0)
-- Dependencies: 226
-- Name: scheduledmaintenance_maintid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.scheduledmaintenance_maintid_seq', 143, true);


--
-- TOC entry 4989 (class 0 OID 0)
-- Dependencies: 227
-- Name: scheduledmaintenance_userid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.scheduledmaintenance_userid_seq', 1, false);


--
-- TOC entry 4990 (class 0 OID 0)
-- Dependencies: 229
-- Name: scheduledresources_resourceid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.scheduledresources_resourceid_seq', 1, false);


--
-- TOC entry 4991 (class 0 OID 0)
-- Dependencies: 230
-- Name: scheduledresources_workid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.scheduledresources_workid_seq', 1, false);


--
-- TOC entry 4992 (class 0 OID 0)
-- Dependencies: 232
-- Name: scheduledwork_userid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.scheduledwork_userid_seq', 1, false);


--
-- TOC entry 4993 (class 0 OID 0)
-- Dependencies: 233
-- Name: scheduledwork_workid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.scheduledwork_workid_seq', 167, true);


--
-- TOC entry 4994 (class 0 OID 0)
-- Dependencies: 235
-- Name: userdata_roleid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.userdata_roleid_seq', 1, false);


--
-- TOC entry 4995 (class 0 OID 0)
-- Dependencies: 236
-- Name: userdata_userid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.userdata_userid_seq', 140, true);


--
-- TOC entry 4996 (class 0 OID 0)
-- Dependencies: 238
-- Name: userroles_roleid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.userroles_roleid_seq', 104, true);


--
-- TOC entry 4761 (class 2606 OID 16530)
-- Name: maintanedresources maintanedresources_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.maintanedresources
    ADD CONSTRAINT maintanedresources_pk PRIMARY KEY (maintid, resourceid);


--
-- TOC entry 4779 (class 2606 OID 16512)
-- Name: maintenancetype maintenancetype_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.maintenancetype
    ADD CONSTRAINT maintenancetype_pk PRIMARY KEY (maintenancetypeid);


--
-- TOC entry 4763 (class 2606 OID 16450)
-- Name: resources resources_resourceId; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resources
    ADD CONSTRAINT "resources_resourceId" PRIMARY KEY (resourceid);


--
-- TOC entry 4765 (class 2606 OID 16452)
-- Name: resourcetypes resourcetypes_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resourcetypes
    ADD CONSTRAINT resourcetypes_pk PRIMARY KEY (typeid);


--
-- TOC entry 4767 (class 2606 OID 16454)
-- Name: scheduledmaintenance scheduledmaintenance_maintId; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scheduledmaintenance
    ADD CONSTRAINT "scheduledmaintenance_maintId" PRIMARY KEY (maintid);


--
-- TOC entry 4769 (class 2606 OID 16532)
-- Name: scheduledresources scheduledresources_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scheduledresources
    ADD CONSTRAINT scheduledresources_pk PRIMARY KEY (workid, resourceid);


--
-- TOC entry 4771 (class 2606 OID 16456)
-- Name: scheduledwork scheduledwork_workId; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scheduledwork
    ADD CONSTRAINT "scheduledwork_workId" PRIMARY KEY (workid);


--
-- TOC entry 4773 (class 2606 OID 16458)
-- Name: userdata userData_userId; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.userdata
    ADD CONSTRAINT "userData_userId" PRIMARY KEY (userid);


--
-- TOC entry 4775 (class 2606 OID 16534)
-- Name: userdata userdata_unique; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.userdata
    ADD CONSTRAINT userdata_unique UNIQUE (email);


--
-- TOC entry 4777 (class 2606 OID 16460)
-- Name: userroles userroles_roleId; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.userroles
    ADD CONSTRAINT "userroles_roleId" PRIMARY KEY (roleid);


--
-- TOC entry 4780 (class 2606 OID 16461)
-- Name: maintanedresources maintanedresources_resources_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.maintanedresources
    ADD CONSTRAINT maintanedresources_resources_fk FOREIGN KEY (resourceid) REFERENCES public.resources(resourceid) ON UPDATE CASCADE;


--
-- TOC entry 4781 (class 2606 OID 16466)
-- Name: maintanedresources maintanedresources_scheduledmaintenance_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.maintanedresources
    ADD CONSTRAINT maintanedresources_scheduledmaintenance_fk FOREIGN KEY (maintid) REFERENCES public.scheduledmaintenance(maintid) ON UPDATE CASCADE;


--
-- TOC entry 4782 (class 2606 OID 16471)
-- Name: resources resources_resourcetypes_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resources
    ADD CONSTRAINT resources_resourcetypes_fk FOREIGN KEY (typeid) REFERENCES public.resourcetypes(typeid) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- TOC entry 4783 (class 2606 OID 16520)
-- Name: scheduledmaintenance scheduledmaintenance_maintenancetype_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scheduledmaintenance
    ADD CONSTRAINT scheduledmaintenance_maintenancetype_fk FOREIGN KEY (maintenancetypeid) REFERENCES public.maintenancetype(maintenancetypeid) ON UPDATE CASCADE;


--
-- TOC entry 4784 (class 2606 OID 16476)
-- Name: scheduledmaintenance scheduledmaintenance_userdata_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scheduledmaintenance
    ADD CONSTRAINT scheduledmaintenance_userdata_fk FOREIGN KEY (userid) REFERENCES public.userdata(userid) ON UPDATE CASCADE;


--
-- TOC entry 4785 (class 2606 OID 16481)
-- Name: scheduledresources scheduledresources_resources_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scheduledresources
    ADD CONSTRAINT scheduledresources_resources_fk FOREIGN KEY (resourceid) REFERENCES public.resources(resourceid) ON UPDATE CASCADE;


--
-- TOC entry 4786 (class 2606 OID 16486)
-- Name: scheduledresources scheduledresources_scheduledwork_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scheduledresources
    ADD CONSTRAINT scheduledresources_scheduledwork_fk FOREIGN KEY (workid) REFERENCES public.scheduledwork(workid) ON UPDATE CASCADE;


--
-- TOC entry 4787 (class 2606 OID 16491)
-- Name: scheduledwork scheduledwork_userdata_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scheduledwork
    ADD CONSTRAINT scheduledwork_userdata_fk FOREIGN KEY (userid) REFERENCES public.userdata(userid);


--
-- TOC entry 4788 (class 2606 OID 16496)
-- Name: userdata userdata_userroles_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.userdata
    ADD CONSTRAINT userdata_userroles_fk FOREIGN KEY (roleid) REFERENCES public.userroles(roleid) ON UPDATE CASCADE;


-- Completed on 2024-10-10 15:19:03

--
-- PostgreSQL database dump complete
--

