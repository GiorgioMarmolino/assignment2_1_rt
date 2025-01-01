### Assignment2 RT

## Ordine di lavoro
1 * scrittura di file .srv e .msg
2 - implementazione dell'action client node
3 - implementazione del service node che ritorna le ultime coordinate inviate


## Informarsi su
	
# action client
	*come si fa un action client
	-come si interfaccia col service corrispondente
	*come si setta il target
	*come si cancella il target
	*feedback/status dell'action server per sapere quando il target è stato raggiunto

# messaggi	
	*come si creano
	-come si usano
	*un custom message per velocità e posizione

# service node
	* file .srv contenente valori posizione
	-come si fa un service node
	-service node che ritorna le ultime coordinate mandate all'action client

# launch file
	-creazione del launchfile


## Applicazioni
# A DONE
	Nodo che implementa action client, prendo in input coordinate (x,y) o le cancella; usare feedback/status di action server per sapere quando il target è stato raggiunto; 	l'action client pubblica di continuo su custom message posizione e velocità basandosi su valori del topic /odom (odometria)

# B
	Service che quando chiamato ritorna le coordinate dell'ultimo target mandato dall'utente all'action server

# C 
	Creazione del launch file per avviare la completa simulazione














# Given specifications:

Create a new package, in which you will develop three nodes:
- (a) A node that implements an action client, allowing the user to set a target (x, y) or to cancel it. Try to use the feedback/status of the action server to know when the target has been reached. The node also publishes the robot position and velocity as a custom message (x,y, vel_x, vel_z), by relying on the values published on the
topic /odom;
- (b) A service node that, when called, returnsthe coordinates of the last target sent by the user;

- Create a launch file to start the whole simulation


