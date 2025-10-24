-- Drop tables if they already exist (optional, to avoid duplication errors)
BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE SALES';
EXCEPTION
    WHEN OTHERS THEN NULL;
END;
/

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE EMPLOYEE';
EXCEPTION
    WHEN OTHERS THEN NULL;
END;
/

BEGIN
    EXECUTE IMMEDIATE 'DROP TABLE PRODUCT';
EXCEPTION
    WHEN OTHERS THEN NULL;
END;
/

-- =============================
-- STEP 1: Create base tables
-- =============================

CREATE TABLE EMPLOYEE (
    EmpId INT PRIMARY KEY,
    EmpName VARCHAR2(50),
    DeptName VARCHAR2(50)
);

CREATE TABLE PRODUCT (
    ProdId VARCHAR2(10) PRIMARY KEY,
    ProdName VARCHAR2(50),
    Price NUMBER(10,2)
);

-- =============================
-- STEP 2: Create SALES table
-- =============================

CREATE TABLE SALES (
    SalesId INT PRIMARY KEY,
    SalesDate DATE DEFAULT CURRENT_DATE,
    Quantity INT NOT NULL,
    EmpId INT,
    ProdId VARCHAR2(10),
    FOREIGN KEY (EmpId) REFERENCES EMPLOYEE(EmpId),
    FOREIGN KEY (ProdId) REFERENCES PRODUCT(ProdId)
);

-- =============================
-- STEP 3: Insert sample data
-- =============================

INSERT INTO EMPLOYEE VALUES (101, 'John', 'HR');
INSERT INTO EMPLOYEE VALUES (102, 'Alice', 'IT');

INSERT INTO PRODUCT VALUES ('P101', 'Laptop', 75000);
INSERT INTO PRODUCT VALUES ('P102', 'Mouse', 500);

INSERT INTO SALES (SalesId, Quantity, EmpId, ProdId)
VALUES (1, 10, 101, 'P101');

INSERT INTO SALES (SalesId, Quantity, EmpId, ProdId)
VALUES (2, 5, 102, 'P102');

COMMIT;

-- =============================
-- STEP 4: Display data
-- =============================

SELECT * FROM SALES;
