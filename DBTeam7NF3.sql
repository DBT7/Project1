-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema TestDB
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema TestDB
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `TestDB` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;

USE `TestDB` ;

-- -----------------------------------------------------
-- Table `TestDB`.`Building`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `TestDB`.`Building` (
  `Building_id` INT NOT NULL COMMENT '',
  `Name` VARCHAR(45) NULL COMMENT '',
  PRIMARY KEY (`Building_id`)  COMMENT '')
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `TestDB`.`Address`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `TestDB`.`Address` (
  `Address` varchar(100) NOT NULL COMMENT '',
  `Building_Building_id` INT NOT NULL COMMENT '',
  PRIMARY KEY (`Address`)  COMMENT '',
  INDEX `fk_Address_Building_idx` (`Building_Building_id` ASC)  COMMENT '',
  CONSTRAINT `fk_Address_Building`
    FOREIGN KEY (`Building_Building_id`)
    REFERENCES `TestDB`.`Building` (`Building_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `TestDB`.`Floor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `TestDB`.`Floor` (
  `Floor_id` INT NOT NULL COMMENT '',
  `Building_Building_id` INT NOT NULL COMMENT '',
  PRIMARY KEY (`Floor_id`)  COMMENT '',
  INDEX `fk_Floor_Building1_idx` (`Building_Building_id` ASC)  COMMENT '',
  CONSTRAINT `fk_Floor_Building1`
    FOREIGN KEY (`Building_Building_id`)
    REFERENCES `TestDB`.`Building` (`Building_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `TestDB`.`Room`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `TestDB`.`Room` (
  `Room_id` INT NOT NULL COMMENT '',
  `Name` VARCHAR(45) NULL COMMENT '',
  `Floor_Floor_id` INT NOT NULL COMMENT '',
  `Capacity` INT NULL COMMENT '',
  PRIMARY KEY (`Room_id`)  COMMENT '',
  INDEX `fk_Room_Floor1_idx` (`Floor_Floor_id` ASC)  COMMENT '',
  CONSTRAINT `fk_Room_Floor1`
    FOREIGN KEY (`Floor_Floor_id`)
    REFERENCES `TestDB`.`Floor` (`Floor_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `TestDB`.`Person`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `TestDB`.`Person` (
  `Person_id` INT NOT NULL COMMENT '',
  `FirstName` VARCHAR(45) NULL COMMENT '',
  `LastName` VARCHAR(45) NULL COMMENT '',
  `Email` VARCHAR(45) NULL COMMENT '',
  PRIMARY KEY (`Person_id`)  COMMENT '')
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `TestDB`.`Admin`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `TestDB`.`Admin` (
  `Admin_id` INT NOT NULL COMMENT '',
  `Person_Person_id` INT NOT NULL COMMENT '',
  PRIMARY KEY (`Admin_id`)  COMMENT '',
  INDEX `fk_Admin_Person1_idx` (`Person_Person_id` ASC)  COMMENT '',
  CONSTRAINT `fk_Admin_Person1`
    FOREIGN KEY (`Person_Person_id`)
    REFERENCES `TestDB`.`Person` (`Person_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `TestDB`.`Manager`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `TestDB`.`Manager` (
  `Manager_id` INT NOT NULL COMMENT '',
  `Admin_Admin_id` INT NOT NULL COMMENT '',
  `Person_Person_id` INT NOT NULL COMMENT '',
  PRIMARY KEY (`Manager_id`)  COMMENT '',
  INDEX `fk_Manager_Admin1_idx` (`Admin_Admin_id` ASC)  COMMENT '',
  INDEX `fk_Manager_Person1_idx` (`Person_Person_id` ASC)  COMMENT '',
  CONSTRAINT `fk_Manager_Admin1`
    FOREIGN KEY (`Admin_Admin_id`)
    REFERENCES `TestDB`.`Admin` (`Admin_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Manager_Person1`
    FOREIGN KEY (`Person_Person_id`)
    REFERENCES `TestDB`.`Person` (`Person_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `TestDB`.`Organization`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `TestDB`.`Organization` (
  `Organization_id` INT NOT NULL COMMENT '',
  `OrgName` VARCHAR(45) NULL COMMENT '',
  PRIMARY KEY (`Organization_id`)  COMMENT '')
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `TestDB`.`User`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `TestDB`.`User` (
  `User_id` INT NOT NULL COMMENT '',
  `ActiveReservations` INT NULL COMMENT '',
  `Manager_Manager_id` INT NOT NULL COMMENT '',
  `Person_Person_id` INT NOT NULL COMMENT '',
  `Organization_Organization_id` INT NOT NULL COMMENT '',
  PRIMARY KEY (`User_id`)  COMMENT '',
  INDEX `fk_User_Manager1_idx` (`Manager_Manager_id` ASC)  COMMENT '',
  INDEX `fk_User_Person1_idx` (`Person_Person_id` ASC)  COMMENT '',
  INDEX `fk_User_Organization1_idx` (`Organization_Organization_id` ASC)  COMMENT '',
  CONSTRAINT `fk_User_Manager1`
    FOREIGN KEY (`Manager_Manager_id`)
    REFERENCES `TestDB`.`Manager` (`Manager_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_User_Person1`
    FOREIGN KEY (`Person_Person_id`)
    REFERENCES `TestDB`.`Person` (`Person_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_User_Organization1`
    FOREIGN KEY (`Organization_Organization_id`)
    REFERENCES `TestDB`.`Organization` (`Organization_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `TestDB`.`Recurrence`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `TestDB`.`Recurrence` (
  `Recurrence_id` INT NOT NULL COMMENT '',
  `Description` VARCHAR(45) NULL COMMENT '',
  PRIMARY KEY (`Recurrence_id`)  COMMENT '')
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `TestDB`.`Reservation`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `TestDB`.`Reservation` (
  `Reservation_id` INT NOT NULL COMMENT '',
  `Reservation_dt` DATETIME NOT NULL COMMENT '',
  `Admin_Admin_id` INT NOT NULL COMMENT '',
  `User_User_id` INT NOT NULL COMMENT '',
  `Manager_Manager_id` INT NOT NULL COMMENT '',
  `Recurrence_Recurrence_id` INT NOT NULL COMMENT '',
  `Room_Room_id` INT NOT NULL COMMENT '',
  PRIMARY KEY (`Reservation_id`)  COMMENT '',
  INDEX `fk_Reservation_Admin1_idx` (`Admin_Admin_id` ASC)  COMMENT '',
  INDEX `fk_Reservation_User1_idx` (`User_User_id` ASC)  COMMENT '',
  INDEX `fk_Reservation_Manager1_idx` (`Manager_Manager_id` ASC)  COMMENT '',
  INDEX `fk_Reservation_Recurrence1_idx` (`Recurrence_Recurrence_id` ASC)  COMMENT '',
  INDEX `fk_Reservation_Room1_idx` (`Room_Room_id` ASC)  COMMENT '',
  CONSTRAINT `fk_Reservation_Admin1`
    FOREIGN KEY (`Admin_Admin_id`)
    REFERENCES `TestDB`.`Admin` (`Admin_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Reservation_User1`
    FOREIGN KEY (`User_User_id`)
    REFERENCES `TestDB`.`User` (`User_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Reservation_Manager1`
    FOREIGN KEY (`Manager_Manager_id`)
    REFERENCES `TestDB`.`Manager` (`Manager_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Reservation_Recurrence1`
    FOREIGN KEY (`Recurrence_Recurrence_id`)
    REFERENCES `TestDB`.`Recurrence` (`Recurrence_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Reservation_Room1`
    FOREIGN KEY (`Room_Room_id`)
    REFERENCES `TestDB`.`Room` (`Room_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `TestDB`.`Resource`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `TestDB`.`Resource` (
  `Projector` TINYINT(1) NOT NULL COMMENT '',
  `Internet` TINYINT(1) NULL COMMENT '',
  `Handicap Access` TINYINT(1) NULL COMMENT '',
  `Chalkboard` TINYINT(1) NULL COMMENT '',
  `Room_Room_id` INT NOT NULL COMMENT '',
  PRIMARY KEY (`Projector`)  COMMENT '',
  INDEX `fk_Resource_Room1_idx` (`Room_Room_id` ASC)  COMMENT '',
  CONSTRAINT `fk_Resource_Room1`
    FOREIGN KEY (`Room_Room_id`)
    REFERENCES `TestDB`.`Room` (`Room_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Data for table `TestDB`.`Building`
-- -----------------------------------------------------
-- START TRANSACTION;
-- USE `TestDB`;
-- INSERT INTO `TestDB`.`Building` (`Building_id`, `Name`) VALUES (01, 'CornerStone');

-- AddressCOMMIT;


-- -----------------------------------------------------
-- Data for table `TestDB`.`Address`
-- -----------------------------------------------------
-- TRANSACTION;
-- USE `TestDB`;
-- INSERT INTO `TestDB`.`Address` (`Address`, `Building_Building_id`) VALUES ('600 S. Captiol St.', 01);
-- COMMIT;


-- -----------------------------------------------------
-- Data for table `TestDB`.`Floor`
-- -----------------------------------------------------
START TRANSACTION;
USE `TestDB`;
INSERT INTO `TestDB`.`Floor` (`Floor_id`, `Building_Building_id`) VALUES (01, 01);

COMMIT;


-- -----------------------------------------------------
-- Data for table `TestDB`.`Room`
-- -----------------------------------------------------
START TRANSACTION;
USE `TestDB`;
INSERT INTO `TestDB`.`Room` (`Room_id`, `Name`, `Floor_Floor_id`, `Capacity`) VALUES (01, 'Conference Room 1', 01, NULL);

COMMIT;


-- -----------------------------------------------------
-- Data for table `TestDB`.`Admin`
-- -----------------------------------------------------
START TRANSACTION;
USE `TestDB`;
INSERT INTO `TestDB`.`Admin` (`Admin_id`, `Person_Person_id`) VALUES (01, DEFAULT);

COMMIT;


-- -----------------------------------------------------
-- Data for table `TestDB`.`Manager`
-- -----------------------------------------------------
START TRANSACTION;
USE `TestDB`;
INSERT INTO `TestDB`.`Manager` (`Manager_id`, `Admin_Admin_id`, `Person_Person_id`) VALUES (01, 01, DEFAULT);

COMMIT;


-- -----------------------------------------------------
-- Data for table `TestDB`.`User`
-- -----------------------------------------------------
START TRANSACTION;
USE `TestDB`;
INSERT INTO `TestDB`.`User` (`User_id`, `ActiveReservations`, `Manager_Manager_id`, `Person_Person_id`, `Organization_Organization_id`) VALUES (01, 0, 01, DEFAULT, DEFAULT);

COMMIT;


-- -----------------------------------------------------
-- Data for table `TestDB`.`Reservation`
-- -----------------------------------------------------
START TRANSACTION;
USE `TestDB`;
INSERT INTO `TestDB`.`Reservation` (`Reservation_id`, `Reservation_dt`, `Admin_Admin_id`, `User_User_id`, `Manager_Manager_id`, `Recurrence_Recurrence_id`, `Room_Room_id`) VALUES (01, '10/6/2015', 01, 01, 01, DEFAULT, DEFAULT);

COMMIT;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
