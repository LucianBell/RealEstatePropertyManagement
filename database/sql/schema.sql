/*
Creating tables to use in DB
*/

/*Properties Table*/

CREATE TABLE Properties (
    PropertyId int NOT NULL,
    Adress VARCHAR(255) NOT NULL,
    PropertyType VARCHAR(255) NOT NULL,
    PropertySize int NOT NULL,
    IsForSale boolean,
    SalePrice int,
    RentalPrice int,
    NumberOfUnits int, 
    PRIMARY KEY (ID)
);
