--
-- PostgreSQL database dump
--

-- Dumped from database version 16.4 (Ubuntu 16.4-0ubuntu0.24.04.2)
-- Dumped by pg_dump version 16.4 (Ubuntu 16.4-0ubuntu0.24.04.2)

-- Started on 2024-09-30 09:42:26 CEST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE "resourceManagement";
--
-- TOC entry 3534 (class 1262 OID 17386)
-- Name: resourceManagement; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE "resourceManagement" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.UTF-8';


ALTER DATABASE "resourceManagement" OWNER TO postgres;

\connect "resourceManagement"

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
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
-- TOC entry 3535 (class 0 OID 0)
-- Dependencies: 5
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 215 (class 1259 OID 17387)
-- Name: maintanedresources; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.maintanedresources (
    maintid integer NOT NULL,
    resourceid integer NOT NULL
);


ALTER TABLE public.maintanedresources OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 17390)
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
-- TOC entry 3536 (class 0 OID 0)
-- Dependencies: 216
-- Name: maintanedresources_maintid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.maintanedresources_maintid_seq OWNED BY public.maintanedresources.maintid;


--
-- TOC entry 217 (class 1259 OID 17391)
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
-- TOC entry 3537 (class 0 OID 0)
-- Dependencies: 217
-- Name: maintanedresources_resourceid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.maintanedresources_resourceid_seq OWNED BY public.maintanedresources.resourceid;


--
-- TOC entry 218 (class 1259 OID 17392)
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
-- TOC entry 3538 (class 0 OID 0)
-- Dependencies: 218
-- Name: TABLE resources; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public.resources IS 'Resources table stores the data about resources';


--
-- TOC entry 219 (class 1259 OID 17398)
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
-- TOC entry 3539 (class 0 OID 0)
-- Dependencies: 219
-- Name: resources_resourceid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.resources_resourceid_seq OWNED BY public.resources.resourceid;


--
-- TOC entry 220 (class 1259 OID 17399)
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
-- TOC entry 3540 (class 0 OID 0)
-- Dependencies: 220
-- Name: resources_typeid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.resources_typeid_seq OWNED BY public.resources.typeid;


--
-- TOC entry 221 (class 1259 OID 17400)
-- Name: resourcetypes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.resourcetypes (
    typeid integer NOT NULL,
    typename character varying NOT NULL
);


ALTER TABLE public.resourcetypes OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 17405)
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
-- TOC entry 3541 (class 0 OID 0)
-- Dependencies: 222
-- Name: resourcetypes_typeid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.resourcetypes_typeid_seq OWNED BY public.resourcetypes.typeid;


--
-- TOC entry 223 (class 1259 OID 17406)
-- Name: scheduledmaintenance; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.scheduledmaintenance (
    maintid integer NOT NULL,
    userid integer NOT NULL,
    fromdate timestamp with time zone NOT NULL,
    duration interval NOT NULL,
    createdate timestamp with time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.scheduledmaintenance OWNER TO postgres;

--
-- TOC entry 224 (class 1259 OID 17410)
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
-- TOC entry 3542 (class 0 OID 0)
-- Dependencies: 224
-- Name: scheduledmaintenance_maintid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.scheduledmaintenance_maintid_seq OWNED BY public.scheduledmaintenance.maintid;


--
-- TOC entry 225 (class 1259 OID 17411)
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
-- TOC entry 3543 (class 0 OID 0)
-- Dependencies: 225
-- Name: scheduledmaintenance_userid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.scheduledmaintenance_userid_seq OWNED BY public.scheduledmaintenance.userid;


--
-- TOC entry 226 (class 1259 OID 17412)
-- Name: scheduledresources; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.scheduledresources (
    workid integer NOT NULL,
    resourceid integer NOT NULL
);


ALTER TABLE public.scheduledresources OWNER TO postgres;

--
-- TOC entry 227 (class 1259 OID 17415)
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
-- TOC entry 3544 (class 0 OID 0)
-- Dependencies: 227
-- Name: scheduledresources_resourceid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.scheduledresources_resourceid_seq OWNED BY public.scheduledresources.resourceid;


--
-- TOC entry 228 (class 1259 OID 17416)
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
-- TOC entry 3545 (class 0 OID 0)
-- Dependencies: 228
-- Name: scheduledresources_workid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.scheduledresources_workid_seq OWNED BY public.scheduledresources.workid;


--
-- TOC entry 229 (class 1259 OID 17417)
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
-- TOC entry 230 (class 1259 OID 17421)
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
-- TOC entry 3546 (class 0 OID 0)
-- Dependencies: 230
-- Name: scheduledwork_userid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.scheduledwork_userid_seq OWNED BY public.scheduledwork.userid;


--
-- TOC entry 231 (class 1259 OID 17422)
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
-- TOC entry 3547 (class 0 OID 0)
-- Dependencies: 231
-- Name: scheduledwork_workid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.scheduledwork_workid_seq OWNED BY public.scheduledwork.workid;


--
-- TOC entry 232 (class 1259 OID 17423)
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
-- TOC entry 3548 (class 0 OID 0)
-- Dependencies: 232
-- Name: TABLE userdata; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public.userdata IS 'This is the userdata table, which stores the user data.';


--
-- TOC entry 233 (class 1259 OID 17429)
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
-- TOC entry 3549 (class 0 OID 0)
-- Dependencies: 233
-- Name: userdata_roleid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.userdata_roleid_seq OWNED BY public.userdata.roleid;


--
-- TOC entry 234 (class 1259 OID 17430)
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
-- TOC entry 3550 (class 0 OID 0)
-- Dependencies: 234
-- Name: userdata_userid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.userdata_userid_seq OWNED BY public.userdata.userid;


--
-- TOC entry 235 (class 1259 OID 17431)
-- Name: userroles; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.userroles (
    roleid integer NOT NULL,
    rolename character varying NOT NULL
);


ALTER TABLE public.userroles OWNER TO postgres;

--
-- TOC entry 236 (class 1259 OID 17436)
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
-- TOC entry 3551 (class 0 OID 0)
-- Dependencies: 236
-- Name: userroles_roleid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.userroles_roleid_seq OWNED BY public.userroles.roleid;


--
-- TOC entry 3326 (class 2604 OID 17437)
-- Name: maintanedresources maintid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.maintanedresources ALTER COLUMN maintid SET DEFAULT nextval('public.maintanedresources_maintid_seq'::regclass);


--
-- TOC entry 3327 (class 2604 OID 17438)
-- Name: maintanedresources resourceid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.maintanedresources ALTER COLUMN resourceid SET DEFAULT nextval('public.maintanedresources_resourceid_seq'::regclass);


--
-- TOC entry 3328 (class 2604 OID 17439)
-- Name: resources resourceid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resources ALTER COLUMN resourceid SET DEFAULT nextval('public.resources_resourceid_seq'::regclass);


--
-- TOC entry 3329 (class 2604 OID 17440)
-- Name: resources typeid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resources ALTER COLUMN typeid SET DEFAULT nextval('public.resources_typeid_seq'::regclass);


--
-- TOC entry 3331 (class 2604 OID 17441)
-- Name: resourcetypes typeid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resourcetypes ALTER COLUMN typeid SET DEFAULT nextval('public.resourcetypes_typeid_seq'::regclass);


--
-- TOC entry 3332 (class 2604 OID 17442)
-- Name: scheduledmaintenance maintid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scheduledmaintenance ALTER COLUMN maintid SET DEFAULT nextval('public.scheduledmaintenance_maintid_seq'::regclass);


--
-- TOC entry 3333 (class 2604 OID 17443)
-- Name: scheduledmaintenance userid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scheduledmaintenance ALTER COLUMN userid SET DEFAULT nextval('public.scheduledmaintenance_userid_seq'::regclass);


--
-- TOC entry 3335 (class 2604 OID 17444)
-- Name: scheduledresources workid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scheduledresources ALTER COLUMN workid SET DEFAULT nextval('public.scheduledresources_workid_seq'::regclass);


--
-- TOC entry 3336 (class 2604 OID 17445)
-- Name: scheduledresources resourceid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scheduledresources ALTER COLUMN resourceid SET DEFAULT nextval('public.scheduledresources_resourceid_seq'::regclass);


--
-- TOC entry 3337 (class 2604 OID 17446)
-- Name: scheduledwork workid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scheduledwork ALTER COLUMN workid SET DEFAULT nextval('public.scheduledwork_workid_seq'::regclass);


--
-- TOC entry 3338 (class 2604 OID 17447)
-- Name: scheduledwork userid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scheduledwork ALTER COLUMN userid SET DEFAULT nextval('public.scheduledwork_userid_seq'::regclass);


--
-- TOC entry 3340 (class 2604 OID 17448)
-- Name: userdata userid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.userdata ALTER COLUMN userid SET DEFAULT nextval('public.userdata_userid_seq'::regclass);


--
-- TOC entry 3342 (class 2604 OID 17449)
-- Name: userdata roleid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.userdata ALTER COLUMN roleid SET DEFAULT nextval('public.userdata_roleid_seq'::regclass);


--
-- TOC entry 3343 (class 2604 OID 17450)
-- Name: userroles roleid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.userroles ALTER COLUMN roleid SET DEFAULT nextval('public.userroles_roleid_seq'::regclass);


--
-- TOC entry 3507 (class 0 OID 17387)
-- Dependencies: 215
-- Data for Name: maintanedresources; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3510 (class 0 OID 17392)
-- Dependencies: 218
-- Data for Name: resources; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.resources VALUES (1, 'test', 1, '{"x":100, "y":300, "z":400}', '2024-09-20 14:48:39.738442+02');


--
-- TOC entry 3513 (class 0 OID 17400)
-- Dependencies: 221
-- Data for Name: resourcetypes; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.resourcetypes VALUES (6, '3d nyomtato 2');
INSERT INTO public.resourcetypes VALUES (7, '3d nyomtato 3');
INSERT INTO public.resourcetypes VALUES (8, '3d nyomtato 4');
INSERT INTO public.resourcetypes VALUES (9, '3d nyomtato 5');
INSERT INTO public.resourcetypes VALUES (1, 'Nyomtato1000');


--
-- TOC entry 3515 (class 0 OID 17406)
-- Dependencies: 223
-- Data for Name: scheduledmaintenance; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3518 (class 0 OID 17412)
-- Dependencies: 226
-- Data for Name: scheduledresources; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3521 (class 0 OID 17417)
-- Dependencies: 229
-- Data for Name: scheduledwork; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3524 (class 0 OID 17423)
-- Dependencies: 232
-- Data for Name: userdata; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.userdata VALUES (1, 'kristof20011020@gmail.com', 'Kristof Mark', 'Jakab', 'password', '2024-09-20 13:04:21.761875+02', 1);


--
-- TOC entry 3527 (class 0 OID 17431)
-- Dependencies: 235
-- Data for Name: userroles; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.userroles VALUES (1, 'Admin');


--
-- TOC entry 3552 (class 0 OID 0)
-- Dependencies: 216
-- Name: maintanedresources_maintid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.maintanedresources_maintid_seq', 1, false);


--
-- TOC entry 3553 (class 0 OID 0)
-- Dependencies: 217
-- Name: maintanedresources_resourceid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.maintanedresources_resourceid_seq', 1, false);


--
-- TOC entry 3554 (class 0 OID 0)
-- Dependencies: 219
-- Name: resources_resourceid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.resources_resourceid_seq', 1, true);


--
-- TOC entry 3555 (class 0 OID 0)
-- Dependencies: 220
-- Name: resources_typeid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.resources_typeid_seq', 1, false);


--
-- TOC entry 3556 (class 0 OID 0)
-- Dependencies: 222
-- Name: resourcetypes_typeid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.resourcetypes_typeid_seq', 28, true);


--
-- TOC entry 3557 (class 0 OID 0)
-- Dependencies: 224
-- Name: scheduledmaintenance_maintid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.scheduledmaintenance_maintid_seq', 1, false);


--
-- TOC entry 3558 (class 0 OID 0)
-- Dependencies: 225
-- Name: scheduledmaintenance_userid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.scheduledmaintenance_userid_seq', 1, false);


--
-- TOC entry 3559 (class 0 OID 0)
-- Dependencies: 227
-- Name: scheduledresources_resourceid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.scheduledresources_resourceid_seq', 1, false);


--
-- TOC entry 3560 (class 0 OID 0)
-- Dependencies: 228
-- Name: scheduledresources_workid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.scheduledresources_workid_seq', 1, false);


--
-- TOC entry 3561 (class 0 OID 0)
-- Dependencies: 230
-- Name: scheduledwork_userid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.scheduledwork_userid_seq', 1, false);


--
-- TOC entry 3562 (class 0 OID 0)
-- Dependencies: 231
-- Name: scheduledwork_workid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.scheduledwork_workid_seq', 1, false);


--
-- TOC entry 3563 (class 0 OID 0)
-- Dependencies: 233
-- Name: userdata_roleid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.userdata_roleid_seq', 1, false);


--
-- TOC entry 3564 (class 0 OID 0)
-- Dependencies: 234
-- Name: userdata_userid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.userdata_userid_seq', 3, true);


--
-- TOC entry 3565 (class 0 OID 0)
-- Dependencies: 236
-- Name: userroles_roleid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.userroles_roleid_seq', 2, true);


--
-- TOC entry 3345 (class 2606 OID 17452)
-- Name: resources resources_resourceId; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resources
    ADD CONSTRAINT "resources_resourceId" PRIMARY KEY (resourceid);


--
-- TOC entry 3347 (class 2606 OID 17454)
-- Name: resourcetypes resourcetypes_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resourcetypes
    ADD CONSTRAINT resourcetypes_pk PRIMARY KEY (typeid);


--
-- TOC entry 3349 (class 2606 OID 17456)
-- Name: scheduledmaintenance scheduledmaintenance_maintId; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scheduledmaintenance
    ADD CONSTRAINT "scheduledmaintenance_maintId" PRIMARY KEY (maintid);


--
-- TOC entry 3351 (class 2606 OID 17458)
-- Name: scheduledwork scheduledwork_workId; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scheduledwork
    ADD CONSTRAINT "scheduledwork_workId" PRIMARY KEY (workid);


--
-- TOC entry 3353 (class 2606 OID 17460)
-- Name: userdata userData_userId; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.userdata
    ADD CONSTRAINT "userData_userId" PRIMARY KEY (userid);


--
-- TOC entry 3355 (class 2606 OID 17462)
-- Name: userroles userroles_roleId; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.userroles
    ADD CONSTRAINT "userroles_roleId" PRIMARY KEY (roleid);


--
-- TOC entry 3356 (class 2606 OID 17463)
-- Name: maintanedresources maintanedresources_resources_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.maintanedresources
    ADD CONSTRAINT maintanedresources_resources_fk FOREIGN KEY (resourceid) REFERENCES public.resources(resourceid) ON UPDATE CASCADE;


--
-- TOC entry 3357 (class 2606 OID 17468)
-- Name: maintanedresources maintanedresources_scheduledmaintenance_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.maintanedresources
    ADD CONSTRAINT maintanedresources_scheduledmaintenance_fk FOREIGN KEY (maintid) REFERENCES public.scheduledmaintenance(maintid) ON UPDATE CASCADE;


--
-- TOC entry 3358 (class 2606 OID 17473)
-- Name: resources resources_resourcetypes_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resources
    ADD CONSTRAINT resources_resourcetypes_fk FOREIGN KEY (typeid) REFERENCES public.resourcetypes(typeid) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- TOC entry 3359 (class 2606 OID 17478)
-- Name: scheduledmaintenance scheduledmaintenance_userdata_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scheduledmaintenance
    ADD CONSTRAINT scheduledmaintenance_userdata_fk FOREIGN KEY (userid) REFERENCES public.userdata(userid) ON UPDATE CASCADE;


--
-- TOC entry 3360 (class 2606 OID 17483)
-- Name: scheduledresources scheduledresources_resources_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scheduledresources
    ADD CONSTRAINT scheduledresources_resources_fk FOREIGN KEY (resourceid) REFERENCES public.resources(resourceid) ON UPDATE CASCADE;


--
-- TOC entry 3361 (class 2606 OID 17488)
-- Name: scheduledresources scheduledresources_scheduledwork_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scheduledresources
    ADD CONSTRAINT scheduledresources_scheduledwork_fk FOREIGN KEY (workid) REFERENCES public.scheduledwork(workid) ON UPDATE CASCADE;


--
-- TOC entry 3362 (class 2606 OID 17493)
-- Name: scheduledwork scheduledwork_userdata_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scheduledwork
    ADD CONSTRAINT scheduledwork_userdata_fk FOREIGN KEY (userid) REFERENCES public.userdata(userid);


--
-- TOC entry 3363 (class 2606 OID 17498)
-- Name: userdata userdata_userroles_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.userdata
    ADD CONSTRAINT userdata_userroles_fk FOREIGN KEY (roleid) REFERENCES public.userroles(roleid) ON UPDATE CASCADE;


-- Completed on 2024-09-30 09:42:26 CEST

--
-- PostgreSQL database dump complete
--

