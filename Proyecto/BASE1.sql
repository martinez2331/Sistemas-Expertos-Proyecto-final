CREATE DATABASE BASE1;
USE BASE1;
CREATE TABLE plc (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    salidas VARCHAR(50),
    protocolo_comunicacion VARCHAR(100),
    tipo_plc VARCHAR(50)
);
INSERT INTO plc (nombre, salidas, protocolo_comunicacion, tipo_plc) VALUES
('Delta SA2', 'relevador', 'RS232', 'sin pantalla HMI'),
('SIMATIC S7-1200', 'transistor npn', 'S7 sobre ISO TCP RFC1006', 'sin pantalla HMI'),
('INVT IVC1', 'transistor pnp', 'Mini DIN8 RS485', 'con pantalla HMI');
