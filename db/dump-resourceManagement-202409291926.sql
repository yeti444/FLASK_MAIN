--
-- PostgreSQL database dump
--

-- Dumped from database version 14.13 (Ubuntu 14.13-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.13 (Ubuntu 14.13-0ubuntu0.22.04.1)

-- Started on 2024-09-29 19:26:00 CEST

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
-- TOC entry 3452 (class 1262 OID 16385)
-- Name: resourceManagement; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE "resourceManagement" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.UTF-8';


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
-- TOC entry 3 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--




ALTER SCHEMA public OWNER TO postgres;

--
-- TOC entry 3453 (class 0 OID 0)
-- Dependencies: 3
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 227 (class 1259 OID 16484)
-- Name: maintanedresources; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.maintanedresources (
    maintid integer NOT NULL,
    resourceid integer NOT NULL
);


ALTER TABLE public.maintanedresources OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 16482)
-- Name: maintanedresources_maintid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.maintanedresources_maintid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.maintanedresources_maintid_seq OWNER TO postgres;

--
-- TOC entry 3454 (class 0 OID 0)
-- Dependencies: 225
-- Name: maintanedresources_maintid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.maintanedresources_maintid_seq OWNED BY public.maintanedresources.maintid;


--
-- TOC entry 226 (class 1259 OID 16483)
-- Name: maintanedresources_resourceid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.maintanedresources_resourceid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.maintanedresources_resourceid_seq OWNER TO postgres;

--
-- TOC entry 3455 (class 0 OID 0)
-- Dependencies: 226
-- Name: maintanedresources_resourceid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.maintanedresources_resourceid_seq OWNED BY public.maintanedresources.resourceid;


--
-- TOC entry 213 (class 1259 OID 16397)
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
-- TOC entry 3456 (class 0 OID 0)
-- Dependencies: 213
-- Name: TABLE resources; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public.resources IS 'Resources table stores the data about resources';


--
-- TOC entry 211 (class 1259 OID 16395)
-- Name: resources_resourceid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.resources_resourceid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.resources_resourceid_seq OWNER TO postgres;

--
-- TOC entry 3457 (class 0 OID 0)
-- Dependencies: 211
-- Name: resources_resourceid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.resources_resourceid_seq OWNED BY public.resources.resourceid;


--
-- TOC entry 212 (class 1259 OID 16396)
-- Name: resources_typeid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.resources_typeid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.resources_typeid_seq OWNER TO postgres;

--
-- TOC entry 3458 (class 0 OID 0)
-- Dependencies: 212
-- Name: resources_typeid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.resources_typeid_seq OWNED BY public.resources.typeid;


--
-- TOC entry 215 (class 1259 OID 16408)
-- Name: resourcetypes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.resourcetypes (
    typeid integer NOT NULL,
    typename character varying NOT NULL
);


ALTER TABLE public.resourcetypes OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 16407)
-- Name: resourcetypes_typeid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.resourcetypes_typeid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.resourcetypes_typeid_seq OWNER TO postgres;

--
-- TOC entry 3459 (class 0 OID 0)
-- Dependencies: 214
-- Name: resourcetypes_typeid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.resourcetypes_typeid_seq OWNED BY public.resourcetypes.typeid;


--
-- TOC entry 224 (class 1259 OID 16469)
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
-- TOC entry 222 (class 1259 OID 16467)
-- Name: scheduledmaintenance_maintid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.scheduledmaintenance_maintid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.scheduledmaintenance_maintid_seq OWNER TO postgres;

--
-- TOC entry 3460 (class 0 OID 0)
-- Dependencies: 222
-- Name: scheduledmaintenance_maintid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.scheduledmaintenance_maintid_seq OWNED BY public.scheduledmaintenance.maintid;


--
-- TOC entry 223 (class 1259 OID 16468)
-- Name: scheduledmaintenance_userid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.scheduledmaintenance_userid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.scheduledmaintenance_userid_seq OWNER TO postgres;

--
-- TOC entry 3461 (class 0 OID 0)
-- Dependencies: 223
-- Name: scheduledmaintenance_userid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.scheduledmaintenance_userid_seq OWNED BY public.scheduledmaintenance.userid;


--
-- TOC entry 221 (class 1259 OID 16440)
-- Name: scheduledresources; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.scheduledresources (
    workid integer NOT NULL,
    resourceid integer NOT NULL
);


ALTER TABLE public.scheduledresources OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 16439)
-- Name: scheduledresources_resourceid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.scheduledresources_resourceid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.scheduledresources_resourceid_seq OWNER TO postgres;

--
-- TOC entry 3462 (class 0 OID 0)
-- Dependencies: 220
-- Name: scheduledresources_resourceid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.scheduledresources_resourceid_seq OWNED BY public.scheduledresources.resourceid;


--
-- TOC entry 219 (class 1259 OID 16438)
-- Name: scheduledresources_workid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.scheduledresources_workid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.scheduledresources_workid_seq OWNER TO postgres;

--
-- TOC entry 3463 (class 0 OID 0)
-- Dependencies: 219
-- Name: scheduledresources_workid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.scheduledresources_workid_seq OWNED BY public.scheduledresources.workid;


--
-- TOC entry 218 (class 1259 OID 16425)
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
-- TOC entry 217 (class 1259 OID 16424)
-- Name: scheduledwork_userid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.scheduledwork_userid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.scheduledwork_userid_seq OWNER TO postgres;

--
-- TOC entry 3464 (class 0 OID 0)
-- Dependencies: 217
-- Name: scheduledwork_userid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.scheduledwork_userid_seq OWNED BY public.scheduledwork.userid;


--
-- TOC entry 216 (class 1259 OID 16423)
-- Name: scheduledwork_workid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.scheduledwork_workid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.scheduledwork_workid_seq OWNER TO postgres;

--
-- TOC entry 3465 (class 0 OID 0)
-- Dependencies: 216
-- Name: scheduledwork_workid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.scheduledwork_workid_seq OWNED BY public.scheduledwork.workid;


--
-- TOC entry 210 (class 1259 OID 16387)
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
-- TOC entry 3466 (class 0 OID 0)
-- Dependencies: 210
-- Name: TABLE userdata; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public.userdata IS 'This is the userdata table, which stores the user data.';


--
-- TOC entry 230 (class 1259 OID 16508)
-- Name: userdata_roleid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.userdata_roleid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.userdata_roleid_seq OWNER TO postgres;

--
-- TOC entry 3467 (class 0 OID 0)
-- Dependencies: 230
-- Name: userdata_roleid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.userdata_roleid_seq OWNED BY public.userdata.roleid;


--
-- TOC entry 209 (class 1259 OID 16386)
-- Name: userdata_userid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.userdata_userid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.userdata_userid_seq OWNER TO postgres;

--
-- TOC entry 3468 (class 0 OID 0)
-- Dependencies: 209
-- Name: userdata_userid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.userdata_userid_seq OWNED BY public.userdata.userid;


--
-- TOC entry 229 (class 1259 OID 16500)
-- Name: userroles; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.userroles (
    roleid integer NOT NULL,
    rolename character varying NOT NULL
);


ALTER TABLE public.userroles OWNER TO postgres;

--
-- TOC entry 228 (class 1259 OID 16499)
-- Name: userroles_roleid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.userroles_roleid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.userroles_roleid_seq OWNER TO postgres;

--
-- TOC entry 3469 (class 0 OID 0)
-- Dependencies: 228
-- Name: userroles_roleid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.userroles_roleid_seq OWNED BY public.userroles.roleid;


--
-- TOC entry 3263 (class 2604 OID 16530)
-- Name: maintanedresources maintid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.maintanedresources ALTER COLUMN maintid SET DEFAULT nextval('public.maintanedresources_maintid_seq'::regclass);


--
-- TOC entry 3264 (class 2604 OID 16531)
-- Name: maintanedresources resourceid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.maintanedresources ALTER COLUMN resourceid SET DEFAULT nextval('public.maintanedresources_resourceid_seq'::regclass);


--
-- TOC entry 3252 (class 2604 OID 16532)
-- Name: resources resourceid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resources ALTER COLUMN resourceid SET DEFAULT nextval('public.resources_resourceid_seq'::regclass);


--
-- TOC entry 3253 (class 2604 OID 16533)
-- Name: resources typeid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resources ALTER COLUMN typeid SET DEFAULT nextval('public.resources_typeid_seq'::regclass);


--
-- TOC entry 3254 (class 2604 OID 16534)
-- Name: resourcetypes typeid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resourcetypes ALTER COLUMN typeid SET DEFAULT nextval('public.resourcetypes_typeid_seq'::regclass);


--
-- TOC entry 3261 (class 2604 OID 16535)
-- Name: scheduledmaintenance maintid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scheduledmaintenance ALTER COLUMN maintid SET DEFAULT nextval('public.scheduledmaintenance_maintid_seq'::regclass);


--
-- TOC entry 3262 (class 2604 OID 16536)
-- Name: scheduledmaintenance userid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scheduledmaintenance ALTER COLUMN userid SET DEFAULT nextval('public.scheduledmaintenance_userid_seq'::regclass);


--
-- TOC entry 3258 (class 2604 OID 16537)
-- Name: scheduledresources workid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scheduledresources ALTER COLUMN workid SET DEFAULT nextval('public.scheduledresources_workid_seq'::regclass);


--
-- TOC entry 3259 (class 2604 OID 16538)
-- Name: scheduledresources resourceid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scheduledresources ALTER COLUMN resourceid SET DEFAULT nextval('public.scheduledresources_resourceid_seq'::regclass);


--
-- TOC entry 3256 (class 2604 OID 16539)
-- Name: scheduledwork workid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scheduledwork ALTER COLUMN workid SET DEFAULT nextval('public.scheduledwork_workid_seq'::regclass);


--
-- TOC entry 3257 (class 2604 OID 16540)
-- Name: scheduledwork userid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scheduledwork ALTER COLUMN userid SET DEFAULT nextval('public.scheduledwork_userid_seq'::regclass);


--
-- TOC entry 3249 (class 2604 OID 16541)
-- Name: userdata userid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.userdata ALTER COLUMN userid SET DEFAULT nextval('public.userdata_userid_seq'::regclass);


--
-- TOC entry 3250 (class 2604 OID 16542)
-- Name: userdata roleid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.userdata ALTER COLUMN roleid SET DEFAULT nextval('public.userdata_roleid_seq'::regclass);


--
-- TOC entry 3265 (class 2604 OID 16543)
-- Name: userroles roleid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.userroles ALTER COLUMN roleid SET DEFAULT nextval('public.userroles_roleid_seq'::regclass);


--
-- TOC entry 3443 (class 0 OID 16484)
-- Dependencies: 227
-- Data for Name: maintanedresources; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3429 (class 0 OID 16397)
-- Dependencies: 213
-- Data for Name: resources; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.resources VALUES (1, 'test', 1, '{"x":100, "y":300, "z":400}', '2024-09-20 14:48:39.738442+02');


--
-- TOC entry 3431 (class 0 OID 16408)
-- Dependencies: 215
-- Data for Name: resourcetypes; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.resourcetypes VALUES (6, '3d nyomtato 2');
INSERT INTO public.resourcetypes VALUES (7, '3d nyomtato 3');
INSERT INTO public.resourcetypes VALUES (8, '3d nyomtato 4');
INSERT INTO public.resourcetypes VALUES (9, '3d nyomtato 5');
INSERT INTO public.resourcetypes VALUES (1, 'Nyomtato1000');


--
-- TOC entry 3440 (class 0 OID 16469)
-- Dependencies: 224
-- Data for Name: scheduledmaintenance; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3437 (class 0 OID 16440)
-- Dependencies: 221
-- Data for Name: scheduledresources; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3434 (class 0 OID 16425)
-- Dependencies: 218
-- Data for Name: scheduledwork; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3426 (class 0 OID 16387)
-- Dependencies: 210
-- Data for Name: userdata; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.userdata VALUES (1, 'kristof20011020@gmail.com', 'Kristof Mark', 'Jakab', 'password', '2024-09-20 13:04:21.761875+02', 1);


--
-- TOC entry 3445 (class 0 OID 16500)
-- Dependencies: 229
-- Data for Name: userroles; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.userroles VALUES (1, 'Admin');


--
-- TOC entry 3470 (class 0 OID 0)
-- Dependencies: 225
-- Name: maintanedresources_maintid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.maintanedresources_maintid_seq', 1, false);


--
-- TOC entry 3471 (class 0 OID 0)
-- Dependencies: 226
-- Name: maintanedresources_resourceid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.maintanedresources_resourceid_seq', 1, false);


--
-- TOC entry 3472 (class 0 OID 0)
-- Dependencies: 211
-- Name: resources_resourceid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.resources_resourceid_seq', 1, true);


--
-- TOC entry 3473 (class 0 OID 0)
-- Dependencies: 212
-- Name: resources_typeid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.resources_typeid_seq', 1, false);


--
-- TOC entry 3474 (class 0 OID 0)
-- Dependencies: 214
-- Name: resourcetypes_typeid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.resourcetypes_typeid_seq', 28, true);


--
-- TOC entry 3475 (class 0 OID 0)
-- Dependencies: 222
-- Name: scheduledmaintenance_maintid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.scheduledmaintenance_maintid_seq', 1, false);


--
-- TOC entry 3476 (class 0 OID 0)
-- Dependencies: 223
-- Name: scheduledmaintenance_userid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.scheduledmaintenance_userid_seq', 1, false);


--
-- TOC entry 3477 (class 0 OID 0)
-- Dependencies: 220
-- Name: scheduledresources_resourceid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.scheduledresources_resourceid_seq', 1, false);


--
-- TOC entry 3478 (class 0 OID 0)
-- Dependencies: 219
-- Name: scheduledresources_workid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.scheduledresources_workid_seq', 1, false);


--
-- TOC entry 3479 (class 0 OID 0)
-- Dependencies: 217
-- Name: scheduledwork_userid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.scheduledwork_userid_seq', 1, false);


--
-- TOC entry 3480 (class 0 OID 0)
-- Dependencies: 216
-- Name: scheduledwork_workid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.scheduledwork_workid_seq', 1, false);


--
-- TOC entry 3481 (class 0 OID 0)
-- Dependencies: 230
-- Name: userdata_roleid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.userdata_roleid_seq', 1, false);


--
-- TOC entry 3482 (class 0 OID 0)
-- Dependencies: 209
-- Name: userdata_userid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.userdata_userid_seq', 3, true);


--
-- TOC entry 3483 (class 0 OID 0)
-- Dependencies: 228
-- Name: userroles_roleid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.userroles_roleid_seq', 2, true);


--
-- TOC entry 3269 (class 2606 OID 16405)
-- Name: resources resources_resourceId; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resources
    ADD CONSTRAINT "resources_resourceId" PRIMARY KEY (resourceid);


--
-- TOC entry 3271 (class 2606 OID 16415)
-- Name: resourcetypes resourcetypes_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resourcetypes
    ADD CONSTRAINT resourcetypes_pk PRIMARY KEY (typeid);


--
-- TOC entry 3275 (class 2606 OID 16476)
-- Name: scheduledmaintenance scheduledmaintenance_maintId; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scheduledmaintenance
    ADD CONSTRAINT "scheduledmaintenance_maintId" PRIMARY KEY (maintid);


--
-- TOC entry 3273 (class 2606 OID 16432)
-- Name: scheduledwork scheduledwork_workId; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scheduledwork
    ADD CONSTRAINT "scheduledwork_workId" PRIMARY KEY (workid);


--
-- TOC entry 3267 (class 2606 OID 16394)
-- Name: userdata userData_userId; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.userdata
    ADD CONSTRAINT "userData_userId" PRIMARY KEY (userid);


--
-- TOC entry 3277 (class 2606 OID 16507)
-- Name: userroles userroles_roleId; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.userroles
    ADD CONSTRAINT "userroles_roleId" PRIMARY KEY (roleid);


--
-- TOC entry 3284 (class 2606 OID 16489)
-- Name: maintanedresources maintanedresources_resources_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.maintanedresources
    ADD CONSTRAINT maintanedresources_resources_fk FOREIGN KEY (resourceid) REFERENCES public.resources(resourceid) ON UPDATE CASCADE;


--
-- TOC entry 3285 (class 2606 OID 16494)
-- Name: maintanedresources maintanedresources_scheduledmaintenance_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.maintanedresources
    ADD CONSTRAINT maintanedresources_scheduledmaintenance_fk FOREIGN KEY (maintid) REFERENCES public.scheduledmaintenance(maintid) ON UPDATE CASCADE;


--
-- TOC entry 3279 (class 2606 OID 16416)
-- Name: resources resources_resourcetypes_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resources
    ADD CONSTRAINT resources_resourcetypes_fk FOREIGN KEY (typeid) REFERENCES public.resourcetypes(typeid) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- TOC entry 3283 (class 2606 OID 16477)
-- Name: scheduledmaintenance scheduledmaintenance_userdata_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scheduledmaintenance
    ADD CONSTRAINT scheduledmaintenance_userdata_fk FOREIGN KEY (userid) REFERENCES public.userdata(userid) ON UPDATE CASCADE;


--
-- TOC entry 3281 (class 2606 OID 16445)
-- Name: scheduledresources scheduledresources_resources_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scheduledresources
    ADD CONSTRAINT scheduledresources_resources_fk FOREIGN KEY (resourceid) REFERENCES public.resources(resourceid) ON UPDATE CASCADE;


--
-- TOC entry 3282 (class 2606 OID 16450)
-- Name: scheduledresources scheduledresources_scheduledwork_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scheduledresources
    ADD CONSTRAINT scheduledresources_scheduledwork_fk FOREIGN KEY (workid) REFERENCES public.scheduledwork(workid) ON UPDATE CASCADE;


--
-- TOC entry 3280 (class 2606 OID 16433)
-- Name: scheduledwork scheduledwork_userdata_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scheduledwork
    ADD CONSTRAINT scheduledwork_userdata_fk FOREIGN KEY (userid) REFERENCES public.userdata(userid);


--
-- TOC entry 3278 (class 2606 OID 16516)
-- Name: userdata userdata_userroles_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.userdata
    ADD CONSTRAINT userdata_userroles_fk FOREIGN KEY (roleid) REFERENCES public.userroles(roleid) ON UPDATE CASCADE;


-- Completed on 2024-09-29 19:26:00 CEST

--
-- PostgreSQL database dump complete
--

