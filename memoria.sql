DROP TABLE IF EXISTS memor;

CREATE TABLE posts(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    titolo TEXT,  
    spiegazione TEXT
);

INSERT INTO  posts(  titolo,  spiegazione) VALUES
('mettere il filamento giallo a essicare ',' ricordati di metterlo a 80 gradi '),
(' mettere in stampa il buddah di Erica ', ' cambia le impostazioni se no non funziona'),
('comprare  qualcosa al elnos',' andare da tiger'),
('andare a pescare con Luca',' ricordarsi di comprare i cagnotti'); 