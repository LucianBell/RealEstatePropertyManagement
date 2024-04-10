ALTER TABLE properties
ADD CONSTRAINT fk_curtenant FOREIGN KEY (CurrentTenant) REFERENCES Tenants(TenantID);

ALTER TABLE tenants
ADD CONSTRAINT fk_rentahist FOREIGN KEY (RentaHistory) REFERENCES RentalHistory(RentalID);

ALTER TABLE rentalhistory
ADD CONSTRAINT fk_tenant FOREIGN KEY (TenantID) REFERENCES Tenants(TenantID);
