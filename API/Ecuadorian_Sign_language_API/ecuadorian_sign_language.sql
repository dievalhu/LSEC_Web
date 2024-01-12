-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 31-10-2023 a las 02:32:46
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `ecuadorian_Sign_Language_base`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `caracter`
--

CREATE TABLE `caracter` (
  `id_caracter` int(11) NOT NULL,
  `caracter` varchar(2) NOT NULL,
  `video` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `caracter`
--

INSERT INTO `caracter` (`id_caracter`, `caracter`, `video`) VALUES
(1, '0', '0.mp4'),
(2, '1', '1.mp4'),
(3, '2', '2.mp4'),
(4, '3', '3.mp4'),
(5, '4', '4.mp4'),
(6, '5', '5.mp4'),
(7, '6', '6.mp4'),
(8, '7', '7.mp4'),
(9, '8', '8.mp4'),
(10, '9', '9.mp4'),
(11, 'a', 'a.mp4'),
(12, 'á', 'a.mp4'),
(13, 'b', 'b.mp4'),
(14, 'c', 'c.mp4'),
(15, 'd', 'd.mp4'),
(16, 'e', 'e.mp4'),
(17, 'é', 'e.mp4'),
(18, 'f', 'f.mp4'),
(19, 'g', 'g.mp4'),
(20, 'h', 'h.mp4'),
(21, 'i', 'i.mp4'),
(22, 'í', 'i.mp4'),
(23, 'j', 'j.mp4'),
(24, 'k', 'k.mp4'),
(25, 'l', 'l.mp4'),
(26, 'm', 'm.mp4'),
(27, 'n', 'n.mp4'),
(28, 'ñ', 'n.mp4'),
(29, 'o', 'o.mp4'),
(30, 'ó', 'o.mp4'),
(31, 'p', 'p.mp4'),
(32, 'q', 'q.mp4'),
(33, 'r', 'r.mp4'),
(34, 's', 's.mp4'),
(35, 't', 't.mp4'),
(36, 'u', 'u.mp4'),
(37, 'ú', 'u.mp4'),
(38, 'v', 'v.mp4'),
(39, 'w', 'w.mp4'),
(40, 'x', 'x.mp4'),
(41, 'y', 'y.mp4'),
(42, 'z', 'z.mp4'),
(43, '{', '{.mp4');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `palabra`
--

CREATE TABLE `palabra` (
  `id_palabra` int(11) NOT NULL,
  `palabra` varchar(100) NOT NULL,
  `descripcion` varchar(200) NOT NULL,
  `video` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `palabra`
--

INSERT INTO `palabra` (`id_palabra`, `palabra`, `descripcion`, `video`) VALUES
(1, 'aceptar', 'aceptar', 'ACEPTAR.mp4'),
(2, 'acusar', 'acusar', 'ACUSAR.mp4'),
(3, 'agalla', 'agalla', 'AGALLA.mp4'),
(4, 'aguila', 'aguila', 'AGUILA.mp4'),
(5, 'albañil', 'albañil', 'ALBAÑIL.mp4'),
(6, 'amadecasa', 'amadecasa', 'AMADECASA.mp4'),
(7, 'amasar', 'amasar', 'AMASAR.mp4'),
(8, 'anfibio', 'anfibio', 'ANFIBIO.mp4'),
(9, 'ansiosa', 'ansiosa', 'ANSIOSA.mp4'),
(10, 'ansioso', 'ansioso', 'ANSIOSO.mp4'),
(11, 'armadillo', 'armadillo', 'ARMADILLO.mp4'),
(12, 'asi', 'asi', 'ASI.mp4'),
(13, 'atraves', 'atraves', 'ATRAVES.mp4'),
(14, 'atropellar', 'atropellar', 'ATROPELLAR.mp4'),
(15, 'automático', 'automático', 'AUTOMÁTICO.mp4'),
(16, 'axila', 'axila', 'AXILA.mp4'),
(17, 'bachillerato', 'bachillerato', 'BACHILLERATO.mp4'),
(18, 'barbon', 'barbon', 'BARBON.mp4'),
(19, 'barrer', 'barrer', 'BARRER.mp4'),
(20, 'bebé', 'bebé', 'BEBÉ.mp4'),
(21, 'billetera', 'billetera', 'BILLETERA.mp4'),
(22, 'bisexual', 'bisexual', 'BISEXUAL.mp4'),
(23, 'blanca', 'blanca', 'BLANCA.mp4'),
(24, 'blanco', 'blanco', 'BLANCO.mp4'),
(25, 'bobo', 'bobo', 'BOBO.mp4'),
(26, 'bocacerrada', 'bocacerrada', 'BOCACERRADA.mp4'),
(27, 'boda', 'boda', 'BODA.mp4'),
(28, 'bolsadevalores', 'bolsadevalores', 'BOLSADEVALORES.mp4'),
(29, 'bolsillo', 'bolsillo', 'BOLSILLO.mp4'),
(30, 'bondad', 'bondad', 'BONDAD.mp4'),
(31, 'bondadoso', 'bondadoso', 'BONDADOSO.mp4'),
(32, 'bostezo', 'bostezo', 'BOSTEZO.mp4'),
(33, 'buena', 'buena', 'BUENA.mp4'),
(34, 'bueno', 'bueno', 'BUENO.mp4'),
(35, 'buenprovecho', 'buenprovecho', 'BUENPROVECHO.mp4'),
(36, 'cachetada', 'cachetada', 'CACHETADA.mp4'),
(37, 'caducada', 'caducada', 'CADUCADA.mp4'),
(38, 'caducado', 'caducado', 'CADUCADO.mp4'),
(39, 'calculadora', 'calculadora', 'CALCULADORA.mp4'),
(40, 'carajo', 'carajo', 'CARAJO.mp4'),
(41, 'carrera', 'carrera', 'CARRERA.mp4'),
(42, 'carretera', 'carretera', 'CARRETERA.mp4'),
(43, 'carton', 'carton', 'CARTON.mp4'),
(44, 'casa', 'casa', 'CASA.mp4'),
(45, 'caspa', 'caspa', 'CASPA.mp4'),
(46, 'causa', 'causa', 'CAUSA.mp4'),
(47, 'cementerio', 'cementerio', 'CEMENTERIO.mp4'),
(48, 'centro', 'centro', 'CENTRO.mp4'),
(49, 'cepillo', 'cepillo', 'CEPILLO.mp4'),
(50, 'chef', 'chef', 'CHEF.mp4'),
(51, 'chequera', 'chequera', 'CHEQUERA.mp4'),
(52, 'chismosa', 'chismosa', 'CHISMOSA.mp4'),
(53, 'chismoso', 'chismoso', 'CHISMOSO.mp4'),
(54, 'chocolate', 'chocolate', 'CHOCOLATE.mp4'),
(55, 'cilantro', 'cilantro', 'CILANTRO.mp4'),
(56, 'colchon', 'colchon', 'COLCHON.mp4'),
(57, 'comadre', 'comadre', 'COMADRE.mp4'),
(58, 'comoestá', 'comoestá', 'COMOESTÁ.mp4'),
(59, 'comparar', 'comparar', 'COMPARAR.mp4'),
(60, 'compartir', 'compartir', 'COMPARTIR.mp4'),
(61, 'comportamiento', 'comportamiento', 'COMPORTAMIENTO.mp4'),
(62, 'compromiso', 'compromiso', 'COMPROMISO.mp4'),
(63, 'comunidad', 'comunidad', 'COMUNIDAD.mp4'),
(64, 'conmuchogusto', 'conmuchogusto', 'CONMUCHOGUSTO.mp4'),
(65, 'consulado', 'consulado', 'CONSULADO.mp4'),
(66, 'contenta', 'contenta', 'CONTENTA.mp4'),
(67, 'contento', 'contento', 'CONTENTO.mp4'),
(68, 'contra', 'contra', 'CONTRA.mp4'),
(69, 'contraparte', 'contraparte', 'CONTRAPARTE.mp4'),
(70, 'cooperar', 'cooperar', 'COOPERAR.mp4'),
(71, 'copiar', 'copiar', 'COPIAR.mp4'),
(72, 'corazon', 'corazon', 'CORAZON.mp4'),
(73, 'cordillera', 'cordillera', 'CORDILLERA.mp4'),
(74, 'corrección', 'corrección', 'CORRECCIÓN.mp4'),
(75, 'corrector', 'corrector', 'CORRECTOR.mp4'),
(76, 'corregir', 'corregir', 'CORREGIR.mp4'),
(77, 'cosa', 'cosa', 'COSA.mp4'),
(78, 'coser', 'coser', 'COSER.mp4'),
(79, 'costurera', 'costurera', 'COSTURERA.mp4'),
(80, 'costurero', 'costurero', 'COSTURERO.mp4'),
(81, 'cruzarlaspiernas', 'cruzarlaspiernas', 'CRUZARLASPIERNAS.mp4'),
(82, 'cuerpo', 'cuerpo', 'CUERPO.mp4'),
(83, 'culantro', 'culantro', 'CULANTRO.mp4'),
(84, 'culpa', 'culpa', 'CULPA.mp4'),
(85, 'culpable', 'culpable', 'CULPABLE.mp4'),
(86, 'cumplida', 'cumplida', 'CUMPLIDA.mp4'),
(87, 'cumplido', 'cumplido', 'CUMPLIDO.mp4'),
(88, 'cumplir', 'cumplir', 'CUMPLIR.mp4'),
(89, 'debajo', 'debajo', 'DEBAJO.mp4'),
(90, 'dedicacion', 'dedicacion', 'DEDICACION.mp4'),
(91, 'defrente', 'defrente', 'DEFRENTE.mp4'),
(92, 'dejar', 'dejar', 'DEJAR.mp4'),
(93, 'delgada', 'delgada', 'DELGADA.mp4'),
(94, 'delgado', 'delgado', 'DELGADO.mp4'),
(95, 'delito', 'delito', 'DELITO.mp4'),
(96, 'despacio', 'despacio', 'DESPACIO.mp4'),
(97, 'despedir', 'despedir', 'DESPEDIR.mp4'),
(98, 'desvio', 'desvio', 'DESVIO.mp4'),
(99, 'diapositiva', 'diapositiva', 'DIAPOSITIVA.mp4'),
(100, 'disculpa', 'disculpa', 'DISCULPA.mp4'),
(101, 'disfrutar', 'disfrutar', 'DISFRUTAR.mp4'),
(102, 'dividirseelgasto', 'dividirseelgasto', 'DIVIDIRSEELGASTO.mp4'),
(103, 'division', 'division', 'DIVISION.mp4'),
(104, 'doblar', 'doblar', 'DOBLAR.mp4'),
(105, 'docente', 'docente', 'DOCENTE.mp4'),
(106, 'ecuavoley', 'ecuavoley', 'ECUAVOLEY.mp4'),
(107, 'embrague', 'embrague', 'EMBRAGUE.mp4'),
(108, 'emocion', 'emocion', 'EMOCION.mp4'),
(109, 'empleadadomestica', 'empleadadomestica', 'EMPLEADADOMESTICA.mp4'),
(110, 'empujar', 'empujar', 'EMPUJAR.mp4'),
(111, 'encaminarse', 'encaminarse', 'ENCAMINARSE.mp4'),
(112, 'encebollado', 'encebollado', 'ENCEBOLLADO.mp4'),
(113, 'encima', 'encima', 'ENCIMA.mp4'),
(114, 'enfermo', 'enfermo', 'ENFERMO.mp4'),
(115, 'enfocar', 'enfocar', 'ENFOCAR.mp4'),
(116, 'enfocarse', 'enfocarse', 'ENFOCARSE.mp4'),
(117, 'enfoque', 'enfoque', 'ENFOQUE.mp4'),
(118, 'enfrentar', 'enfrentar', 'ENFRENTAR.mp4'),
(119, 'enfrente', 'enfrente', 'ENFRENTE.mp4'),
(120, 'ensalada', 'ensalada', 'ENSALADA.mp4'),
(121, 'entrar', 'entrar', 'ENTRAR.mp4'),
(122, 'entregar', 'entregar', 'ENTREGAR.mp4'),
(123, 'entusiasmarse', 'entusiasmarse', 'ENTUSIASMARSE.mp4'),
(124, 'epoca', 'epoca', 'EPOCA.mp4'),
(125, 'escalera', 'escalera', 'ESCALERA.mp4'),
(126, 'escolar', 'escolar', 'ESCOLAR.mp4'),
(127, 'espalda', 'espalda', 'ESPALDA.mp4'),
(128, 'especialidad', 'especialidad', 'ESPECIALIDAD.mp4'),
(129, 'especialista', 'especialista', 'ESPECIALISTA.mp4'),
(130, 'especializarce', 'especializarce', 'ESPECIALIZARCE.mp4'),
(131, 'espejo', 'espejo', 'ESPEJO.mp4'),
(132, 'estafa', 'estafa', 'ESTAFA.mp4'),
(133, 'estafador', 'estafador', 'ESTAFADOR.mp4'),
(134, 'estafadora', 'estafadora', 'ESTAFADORA.mp4'),
(135, 'estafar', 'estafar', 'ESTAFAR.mp4'),
(136, 'estarhastalacoronilla', 'estarhastalacoronilla', 'ESTARHASTALACORONILLA.mp4'),
(137, 'estrecho', 'estrecho', 'ESTRECHO.mp4'),
(138, 'estupefacta', 'estupefacta', 'ESTUPEFACTA.mp4'),
(139, 'etapa', 'etapa', 'ETAPA.mp4'),
(140, 'eterna', 'eterna', 'ETERNA.mp4'),
(141, 'eterno', 'eterno', 'ETERNO.mp4'),
(142, 'excepcionalmente', 'excepcionalmente', 'EXCEPCIONALMENTE.mp4'),
(143, 'exprimidor', 'exprimidor', 'EXPRIMIDOR.mp4'),
(144, 'fábrica', 'fábrica', 'FÁBRICA.mp4'),
(145, 'fabricar', 'fabricar', 'FABRICAR.mp4'),
(146, 'facil', 'facil', 'FACIL.mp4'),
(147, 'factura', 'factura', 'FACTURA.mp4'),
(148, 'falda', 'falda', 'FALDA.mp4'),
(149, 'fanesca', 'fanesca', 'FANESCA.mp4'),
(150, 'feliz', 'feliz', 'FELIZ.mp4'),
(151, 'fin', 'fin', 'FIN.mp4'),
(152, 'florero', 'florero', 'FLORERO.mp4'),
(153, 'foca', 'foca', 'FOCA.mp4'),
(154, 'fotocopiar', 'fotocopiar', 'FOTOCOPIAR.mp4'),
(155, 'fracasar', 'fracasar', 'FRACASAR.mp4'),
(156, 'fracaso', 'fracaso', 'FRACASO.mp4'),
(157, 'freir', 'freir', 'FREIR.mp4'),
(158, 'frente', 'frente', 'FRENTE.mp4'),
(159, 'fritura', 'fritura', 'FRITURA.mp4'),
(160, 'frontal', 'frontal', 'FRONTAL.mp4'),
(161, 'fuera', 'fuera', 'FUERA.mp4'),
(162, 'fumador', 'fumador', 'FUMADOR.mp4'),
(163, 'fumadora', 'fumadora', 'FUMADORA.mp4'),
(164, 'fusible', 'fusible', 'FUSIBLE.mp4'),
(165, 'futuro', 'futuro', 'FUTURO.mp4'),
(166, 'gastronomia', 'gastronomia', 'GASTRONOMIA.mp4'),
(167, 'gatear', 'gatear', 'GATEAR.mp4'),
(168, 'generosa', 'generosa', 'GENEROSA.mp4'),
(169, 'generoso', 'generoso', 'GENEROSO.mp4'),
(170, 'golpe', 'golpe', 'GOLPE.mp4'),
(171, 'golpear', 'golpear', 'GOLPEAR.mp4'),
(172, 'gracias', 'gracias', 'GRACIAS.mp4'),
(173, 'grasa', 'grasa', 'GRASA.mp4'),
(174, 'gratis', 'gratis', 'GRATIS.mp4'),
(175, 'gritodeguerra', 'gritodeguerra', 'GRITODEGUERRA.mp4'),
(176, 'grosero', 'grosero', 'GROSERO.mp4'),
(177, 'guardarselainformación', 'guardarselainformación', 'GUARDARSELAINFORMACIÓN.mp4'),
(178, 'guarderia', 'guarderia', 'GUARDERIA.mp4'),
(179, 'guata', 'guata', 'GUATA.mp4'),
(180, 'guitarra', 'guitarra', 'GUITARRA.mp4'),
(181, 'heladodemáquina', 'heladodemáquina', 'HELADODEMÁQUINA.mp4'),
(182, 'hipoacúsico', 'hipoacúsico', 'HIPOACÚSICO.mp4'),
(183, 'humildad', 'humildad', 'HUMILDAD.mp4'),
(184, 'humilde', 'humilde', 'HUMILDE.mp4'),
(185, 'imitar', 'imitar', 'IMITAR.mp4'),
(186, 'íntima', 'íntima', 'ÍNTIMA.mp4'),
(187, 'íntimo', 'íntimo', 'ÍNTIMO.mp4'),
(188, 'lactar', 'lactar', 'LACTAR.mp4'),
(189, 'ladrillo', 'ladrillo', 'LADRILLO.mp4'),
(190, 'lagartija', 'lagartija', 'LAGARTIJA.mp4'),
(191, 'lanzada', 'lanzada', 'LANZADA.mp4'),
(192, 'lanzado', 'lanzado', 'LANZADO.mp4'),
(193, 'lavadora', 'lavadora', 'LAVADORA.mp4'),
(194, 'levantar', 'levantar', 'LEVANTAR.mp4'),
(195, 'levantarse', 'levantarse', 'LEVANTARSE.mp4'),
(196, 'libro', 'libro', 'LIBRO.mp4'),
(197, 'llamar', 'llamar', 'LLAMAR.mp4'),
(198, 'llamarse', 'llamarse', 'LLAMARSE.mp4'),
(199, 'llanura', 'llanura', 'LLANURA.mp4'),
(200, 'llevar1', 'llevar1', 'LLEVAR1.mp4'),
(201, 'loba', 'loba', 'LOBA.mp4'),
(202, 'mamífero', 'mamífero', 'MAMÍFERO.mp4'),
(203, 'menopausia', 'menopausia', 'MENOPAUSIA.mp4'),
(204, 'mula', 'mula', 'MULA.mp4'),
(205, 'nunca', 'nunca', 'NUNCA.mp4'),
(206, 'oregano', 'oregano', 'OREGANO.mp4'),
(207, 'palma', 'palma', 'PALMA.mp4'),
(208, 'panela', 'panela', 'PANELA.mp4'),
(209, 'pantufla', 'pantufla', 'PANTUFLA.mp4'),
(210, 'pañal', 'pañal', 'PAÑAL.mp4'),
(211, 'pañuelo', 'pañuelo', 'PAÑUELO.mp4'),
(212, 'papa', 'papa', 'PAPA.mp4'),
(213, 'parar', 'parar', 'PARAR.mp4'),
(214, 'peces', 'peces', 'PECES.mp4'),
(215, 'pedir', 'pedir', 'PEDIR.mp4'),
(216, 'pegar', 'pegar', 'PEGAR.mp4'),
(217, 'pelear', 'pelear', 'PELEAR.mp4'),
(218, 'pena', 'pena', 'PENA.mp4'),
(219, 'pendeja', 'pendeja', 'PENDEJA.mp4'),
(220, 'perforadora', 'perforadora', 'PERFORADORA.mp4'),
(221, 'periodista', 'periodista', 'PERIODISTA.mp4'),
(222, 'pesame', 'pesame', 'PESAME.mp4'),
(223, 'pesas', 'pesas', 'PESAS.mp4'),
(224, 'pescado', 'pescado', 'PESCADO.mp4'),
(225, 'piñata', 'piñata', 'PIÑATA.mp4'),
(226, 'piston', 'piston', 'PISTON.mp4'),
(227, 'propuesta', 'propuesta', 'PROPUESTA.mp4'),
(228, 'psicologia', 'psicologia', 'PSICOLOGIA.mp4'),
(229, 'quedice', 'quedice', 'QUEDICE.mp4'),
(230, 'quemecuentas', 'quemecuentas', 'QUEMECUENTAS.mp4'),
(231, 'quieto', 'quieto', 'QUIETO.mp4'),
(232, 'quiza', 'quiza', 'QUIZA.mp4'),
(233, 'remolque', 'remolque', 'REMOLQUE.mp4'),
(234, 'respirar', 'respirar', 'RESPIRAR.mp4'),
(235, 'sala', 'sala', 'SALA.mp4'),
(236, 'salami', 'salami', 'SALAMI.mp4'),
(237, 'saldeaqui', 'saldeaqui', 'SALDEAQUI.mp4'),
(238, 'saludar', 'saludar', 'SALUDAR.mp4'),
(239, 'saludo', 'saludo', 'SALUDO.mp4'),
(240, 'seguridadaeroportuaria', 'seguridadaeroportuaria', 'SEGURIDADAEROPORTUARIA.mp4'),
(241, 'servicio', 'servicio', 'SERVICIO.mp4'),
(242, 'servilleta', 'servilleta', 'SERVILLETA.mp4'),
(243, 'servir', 'servir', 'SERVIR.mp4'),
(244, 'siesta', 'siesta', 'SIESTA.mp4'),
(245, 'sindinero', 'sindinero', 'Sindinero.mp4'),
(246, 'sobrina', 'sobrina', 'SOBRINA.mp4'),
(247, 'sobrino', 'sobrino', 'SOBRINO.mp4'),
(248, 'su', 'su', 'SU.mp4'),
(249, 'subir', 'subir', 'SUBIR.mp4'),
(250, 'suyo', 'suyo', 'SUYO.mp4'),
(251, 'tacaña', 'tacaña', 'TACAÑA.mp4'),
(252, 'tacaño', 'tacaño', 'TACAÑO.mp4'),
(253, 'talvez', 'talvez', 'TALVEZ.mp4'),
(254, 'tapar', 'tapar', 'TAPAR.mp4'),
(255, 'taxi', 'taxi', 'TAXI.mp4'),
(256, 'television', 'television', 'TELEVISION.mp4'),
(257, 'temeraria', 'temeraria', 'TEMERARIA.mp4'),
(258, 'temporal', 'temporal', 'TEMPORAL.mp4'),
(259, 'terminar', 'terminar', 'TERMINAR.mp4'),
(260, 'tienda', 'tienda', 'TIENDA.mp4'),
(261, 'tocino', 'tocino', 'TOCINO.mp4'),
(262, 'todo', 'todo', 'TODO.mp4'),
(263, 'todoeldía', 'todoeldía', 'TODOELDÍA.mp4'),
(264, 'tomar', 'tomar', 'TOMAR.mp4'),
(265, 'torear', 'torear', 'TOREAR.mp4'),
(266, 'torera', 'torera', 'TORERA.mp4'),
(267, 'torero', 'torero', 'TORERO.mp4'),
(268, 'torturar', 'torturar', 'TORTURAR.mp4'),
(269, 'universidad', 'universidad', 'UNIVERSIDAD.mp4'),
(270, 'usada', 'usada', 'USADA.mp4'),
(271, 'usado', 'usado', 'USADO.mp4'),
(272, 'usar', 'usar', 'USAR.mp4'),
(273, 'utilizar', 'utilizar', 'UTILIZAR.mp4'),
(274, 'vivienda', 'vivienda', 'VIVIENDA.mp4'),
(275, 'yanomas', 'yanomas', 'YANOMAS.mp4'),
(276, 'testeo', 'testeo', 'TESTEO.mp4'),
(277, 'testeo1', 'testeo1', 'TESTEO1.mp4'),
(278, 'testeo4', 'testeo4', 'TESTEO4.mp4');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `password`) VALUES
(1, 'admin', 'jcajasp2@est.ups.edu.ec', 'tesis.root1'),
(2, 'admin', 'jcajasp2@est.ups.edu.ec', 'tesis.root1'),
(3, 'admin', 'admin1', 'admin1');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `caracter`
--
ALTER TABLE `caracter`
  ADD PRIMARY KEY (`id_caracter`);

--
-- Indices de la tabla `palabra`
--
ALTER TABLE `palabra`
  ADD PRIMARY KEY (`id_palabra`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `caracter`
--
ALTER TABLE `caracter`
  MODIFY `id_caracter` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=44;

--
-- AUTO_INCREMENT de la tabla `palabra`
--
ALTER TABLE `palabra`
  MODIFY `id_palabra` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=279;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
