-- -------------------------------------------------------------
-- TablePlus 6.6.5(626)
--
-- https://tableplus.com/
--
-- Database: bases_curso.sqlite3
-- Generation Time: 2025-07-09 07:27:34.6930
-- -------------------------------------------------------------


CREATE TABLE "clientes" (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nombre TEXT NOT NULL,
	apellido TEXT NOT NULL,
	email TEXT NOT NULL,
	fecha_registro DATETIME NOT NULL,
	telefono INTEGER
, role TEXT);

INSERT INTO "clientes" ("id", "nombre", "apellido", "email", "fecha_registro", "telefono", "role") VALUES
('1', 'Juan Manuel', 'Alvarez', 'juanmadev@icloud.com', '2025-07-07 8:41:40.552583', '3012966226', NULL),
('2', 'Abel', 'Alvarez', 'abelal@icloud.com', '2025-07-07 8:41:40.552583', '3012966226', NULL),
('3', 'Obi', 'Wan', 'obi@bi.com', '2025-07-07 8:41:40.552583', '3012966226', NULL),
('5', 'Scarlett', 'Wan', 'obi@bi.com', '2025-07-07 8:41:40.552583', '3012966226', NULL),
('6', 'Carlos', 'Alvarez', 'abelal@icloud.com', '2025-07-07 8:41:40.552583', '3012966226', NULL),
('7', 'Jaime', 'Perez', 'obi@bi.com', '2025-07-07 8:41:40.552583', '3012966226', NULL),
('8', 'Esteban', 'Wan', 'obi@bi.com', '2025-07-07 8:41:40.552583', '3012966226', NULL),
('9', 'Gloria', 'Alvarez', 'abelal@icloud.com', '2025-07-07 8:41:40.552583', '3012966226', NULL),
('10', 'Tulio', 'Wan', 'obi@bi.com', '2025-07-07 8:41:40.552583', '3012966226', NULL),
('11', 'David', 'Wan', 'obi@bi.com', '2025-07-07 8:41:40.552583', '3012966226', NULL),
('13', 'Andrea', 'Uribe', 'juanmadev@icloud.com', '2025-07-07 8:41:40.552583', '3012966226', NULL),
('14', 'Julieta', 'Perez', 'jma@jma.com', '2025-07-07 8:41:40.552583', '3012966226', NULL);
