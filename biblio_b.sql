-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : ven. 23 juin 2023 à 09:16
-- Version du serveur : 5.7.36
-- Version de PHP : 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `biblio_b`
--

-- --------------------------------------------------------

--
-- Structure de la table `film`
--

DROP TABLE IF EXISTS `film`;
CREATE TABLE IF NOT EXISTS `film` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `annee_sortie` varchar(255) DEFAULT NULL,
  `realisateur` varchar(255) DEFAULT NULL,
  `Titre` varchar(255) DEFAULT NULL,
  `duree` varchar(255) DEFAULT NULL,
  `descrption` varchar(255) DEFAULT NULL,
  `langue` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `film`
--

INSERT INTO `film` (`id`, `annee_sortie`, `realisateur`, `Titre`, `duree`, `descrption`, `langue`) VALUES
(1, '2017', 'Michael Bay', 'Transformers: The Last Knight', '2h 29m', 'The Last Knight fait voler en éclats les mythes essentiels de la franchise Transformers, et redéfinit ce que signifie être un héros. Humains et Transformers sont en guerre.', 'Anlais'),
(2, '2023', 'Ayataka Tanemura', 'black clover sword of the wizard king', '1h 59m', 'Il défie le rêve d\'Asta de devenir empereur mage et défie ses idéaux à travers des épreuves, la découverte de soi et une détermination inébranlable, résonnant avec les fans à un niveau profond.', 'Japan');

-- --------------------------------------------------------

--
-- Structure de la table `livre`
--

DROP TABLE IF EXISTS `livre`;
CREATE TABLE IF NOT EXISTS `livre` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ref_livre` varchar(35) DEFAULT NULL,
  `Titre` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `auteur` varchar(255) DEFAULT NULL,
  `date_parution` varchar(255) DEFAULT NULL,
  `maison_edition` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ref_livre` (`ref_livre`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `livre`
--

INSERT INTO `livre` (`id`, `ref_livre`, `Titre`, `description`, `auteur`, `date_parution`, `maison_edition`) VALUES
(5, '13257', 'harry potter', 'magie', 'J. K. Rowling', '16/11/2001', 'Bloomsbury Publishing'),
(6, '32456', 'alice au pays des merveilles', 'fantastique', 'Lewis Carroll', '5/03/2010', 'Macmillan and Co');

-- --------------------------------------------------------

--
-- Structure de la table `personne`
--

DROP TABLE IF EXISTS `personne`;
CREATE TABLE IF NOT EXISTS `personne` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) DEFAULT NULL,
  `prenom` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `personne`
--

INSERT INTO `personne` (`id`, `nom`, `prenom`) VALUES
(1, 'Kouame', 'Aya'),
(2, 'Diallo', 'Samba'),
(3, 'Diop', 'Aissatou'),
(4, 'Sow', 'Ousmane'),
(5, 'Keita', 'Mariam');

-- --------------------------------------------------------

--
-- Structure de la table `pret`
--

DROP TABLE IF EXISTS `pret`;
CREATE TABLE IF NOT EXISTS `pret` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date_pret` date DEFAULT NULL,
  `date_retour` date DEFAULT NULL,
  `id_Livre` int(11) DEFAULT NULL,
  `id_Personne` int(11) DEFAULT NULL,
  `id_Film` int(11) DEFAULT NULL,
  `rendu` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_Pret_id_Livre` (`id_Livre`),
  KEY `FK_Pret_id_Personne` (`id_Personne`),
  KEY `FK_Pret_id_Film` (`id_Film`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `pret`
--

INSERT INTO `pret` (`id`, `date_pret`, `date_retour`, `id_Livre`, `id_Personne`, `id_Film`, `rendu`) VALUES
(1, '2023-06-22', '2023-06-23', NULL, 3, 1, 0),
(2, '2023-06-20', '2023-06-21', NULL, 4, 2, 0);

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `pret`
--
ALTER TABLE `pret`
  ADD CONSTRAINT `FK_Pret_id_Film` FOREIGN KEY (`id_Film`) REFERENCES `film` (`id`),
  ADD CONSTRAINT `FK_Pret_id_Livre` FOREIGN KEY (`id_Livre`) REFERENCES `livre` (`id`),
  ADD CONSTRAINT `FK_Pret_id_Personne` FOREIGN KEY (`id_Personne`) REFERENCES `personne` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
