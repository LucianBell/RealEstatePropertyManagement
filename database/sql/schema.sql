/*
Creating tables to use in DB
*/

/*Properties Table*/

CREATE TABLE Properties (
    PropertyID INT NOT NULL,
    Adress VARCHAR(255) NOT NULL,
    PropertyType VARCHAR(255) NOT NULL,
    PropertySize INT NOT NULL,
    IsForSale BOOLEAN,
    SalePrice INT,
    RentalPrice INT,
    NumberOfUnits INT,
    CurrentTenant INT, 
    PRIMARY KEY (PropertyID)
);

/*Tenants Table*/

CREATE TABLE Tenants (
    TenantID INT NOT NULL,
    EmploymentStatus VARCHAR(255) NOT NULL,
    ContactEmail VARCHAR(255) NOT NULL,
    EmerNumber VARCHAR(255) NOT NULL,
    MoveInDate DATE NOT NULL,
    RentaHistory INT,
    CreditScore INT,
    PRIMARY KEY (TenantID)
);

CREATE TABLE RentalHistory (
    RentalID INT NOT NULL,
    TenantID INT NOT NULL,
    PreviousProperty VARCHAR(255),
    PreviousMoveInDate DATE,
    PreviousMoveOutDate DATE,
    ReasonForLeaving VARCHAR(255),
    FeedbackGrade INT CHECK (FeedbackGrade >= 0 AND FeedbackGrade <= 5),
    PRIMARY KEY (RentalID)
)
