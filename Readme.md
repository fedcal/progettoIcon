# Progetto Icon - Federico Calò matricola 678191

L'intento del progetto che si è sviluppato consiste nel


Il dataset akas.tsv contiene le seguenti informazioni per i titoli:

- titleId (stringa): a tconst, un identificatore univoco alfanumerico del titolo
- ordering (intero): un numero per identificare in modo univoco le righe per un dato titleId
- title (stringa): il titolo localizzato
- region (string): la regione per questa versione del titolo
- language (string): la lingua del titolo
- types (array): Insieme enumerato di attributi per questo titolo alternativo. Uno o più dei seguenti: "alternative", "dvd", "festival", "tv", "video", "working", "original", "imdbDisplay". Nuovi valori possono essere aggiunti in futuro senza preavviso
- attributes (array): Termini aggiuntivi per descrivere questo titolo alternativo, non enumerati
- isOriginalTitle (booleano): 0: titolo non originale; 1: titolo originale


Il dataset basics.tsv contiene le seguenti informazioni per i titoli:
- tconst (stringa) - identificatore univoco alfanumerico del titolo
- titleType (stringa) – il tipo/formato del titolo (es. film, cortometraggio, serie tv, episodio televisivo, video, ecc.)
- primaryTitle (stringa) – il titolo più popolare/il titolo utilizzato dai registi sui materiali promozionali al momento del rilascio
- originalTitle (stringa) - titolo originale, nella lingua originale
- isAdult (booleano) - 0: titolo non adulto; 1: titolo adulto
- startYear (YYYY) – rappresenta l'anno di uscita di un titolo. Nel caso delle serie TV, è l'anno di inizio della serie
- endYear (YYYY) – Serie TV di fine anno. '\N' per tutti gli altri tipi di titolo
- runtimeMinutes – runtime principale del titolo, in minuti
- generi (array di stringhe) – include fino a tre generi associati al titolo

Il dataset crew.tsv contiene le informazioni su regista e sceneggiatore per tutti i titoli in IMDb. I campi includono:
- tconst (stringa) - identificatore univoco alfanumerico del titolo
- directors (array of nconsts) - director(s) del titolo dato
- writers (array of nconsts) – writer(s) del titolo dato

Il dataset episode.tsv contiene le informazioni sull'episodio televisivo. I campi includono:
- tconst (stringa) - identificatore alfanumerico dell'episodio
- parentTconst (stringa) - identificatore alfanumerico della serie TV principale
- seasonNumber (intero) – numero di stagione a cui appartiene l'episodio
- episodeNumber  (intero) – numero episodio del tconst nella serie TV

principals.tsv contiene il cast/la troupe principale per i titoli
- tconst (stringa) - identificatore univoco alfanumerico del titolo
- ordering (intero) – un numero per identificare in modo univoco le righe per un dato titleId
- nconst (stringa) - identificatore univoco alfanumerico del nome/persona
- category (stringa) - la categoria di lavoro in cui si trovava la persona
- job (string) - il titolo di lavoro specifico se applicabile, altrimenti '\N'
- characters  (stringa) - il nome del carattere riprodotto se applicabile, altrimenti '\N'

ratings.tsv contiene le informazioni sulla valutazione e sui voti di IMDb per i titoli
- tconst (stringa) - identificatore univoco alfanumerico del titolo
- averageRating – media ponderata di tutte le valutazioni dei singoli utenti
- numVotes - numero di voti ricevuti dal titolo

basics.tsv contiene le seguenti informazioni per i nomi:
- nconst (stringa) - identificatore univoco alfanumerico del nome/persona
- primaryName (stringa)– nome con cui la persona viene spesso accreditata
- birthYear  – nel formato AAAA
- deathYear – nel formato AAAA se applicabile, altrimenti '\N'
- primaryProfession (array di stringhe) – le prime 3 professioni della persona
- knownForTitles (array di tconsts) – titoli per cui la persona è nota
## Risorse
Link dataset: https://www.imdb.com/interfaces/