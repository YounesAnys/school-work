import java.util.Random;
import java.util.concurrent.Semaphore;

public class Lab4
{
  // Configuration
  final static int PORT0 = 0;
  final static int PORT1 = 1;
  final static int MAXLOAD = 10;

  public static void main(String args[]) {
     int NUM_CARS = 10;
     int NUM_AMBS = 5;
     int NUM_CROSSING = 10;
    int i;
    
    System.out.println ("num args: " + args.length);
    if (args.length > 0) {
      try {
        NUM_CROSSING = Integer.parseInt(args[0]);
      } catch (NumberFormatException e) {}
    }
    if (args.length > 1) {
      try {
        NUM_CARS = Integer.parseInt(args[1]);
      } catch (NumberFormatException e) {}
    }
    if (args.length > 2) {
      try {
        NUM_AMBS = Integer.parseInt(args[2]);
      } catch (NumberFormatException e) {}
    }

    Ferry ferry = new Ferry(PORT0,NUM_CROSSING);

    Auto [] automobile = new Auto[NUM_CARS];
    for (i=0; i< 7; i++) automobile[i] = new Auto(i,PORT0,ferry);
    for ( ; i<NUM_CARS ; i++) automobile[i] = new Auto(i,PORT1,ferry);

    Ambulance [] ambulance = new Ambulance[NUM_AMBS];
    for (i=0; i< NUM_AMBS; i++) ambulance[i] = new Ambulance(i, (PORT0+i) % 2,ferry);

    /* Start the threads */
    ferry.start();   // Start the ferry thread.
    for (i=0; i<NUM_CARS; i++) automobile[i].start();  // Start automobile threads
    for (i=0; i<NUM_AMBS; i++) ambulance[i].start();  // Start the ambulance thread.

    try {ferry.join();} catch(InterruptedException e) { }; // Wait until ferry terminates.
    System.out.println("Ferry stopped.");
    // Stop other threads.
    for (i=0; i<NUM_CARS; i++) automobile[i].interrupt(); // Let's stop the auto threads.
    for (i=0; i<NUM_AMBS; i++) ambulance[i].interrupt(); // Stop the ambulance thread.
  }
}


class Auto extends Thread { // Class for the auto threads.

  private int id_auto;
  private int port;
  private Ferry fry;
  // private Semaphore semaphore;

  public Auto(int id, int prt, Ferry ferry)
  {
    this.id_auto = id;
    this.port = prt;
    this.fry = ferry;
  }

  public void run() {
    Semaphore semaphore;
    while (true) {
      // Delay
      try {sleep((int) (300*Math.random()));} catch (Exception e) { break;}
      System.out.println("Auto " + id_auto + " arrives at port " + port);
      
      // Set the semaphore
      if (port == Lab4.PORT0) semaphore = fry.semPort[0];
      else semaphore = fry.semPort[1];

      // Board
      try{semaphore.acquire();} catch (InterruptedException e) { break; }
      System.out.println("Auto " + id_auto + " boards on the ferry at port " + port);
      
      fry.addLoad();  // increment the ferry load
      
      if(fry.getLoad() == Lab4.MAXLOAD) fry.semDeparture.release(); 
      else semaphore.release();

      // Arrive at the next port
      port = 1 - port ;   
      
      // Set the semaphore
      if(port == 0) semaphore = fry.semPort[0];
      else semaphore = fry.semPort[1];

      // disembark
      try{fry.semFerryLoad.acquire();} catch (InterruptedException e) { break; }    
      System.out.println("Auto " + id_auto + " disembarks from ferry at port " + port);
      
      fry.reduceLoad();   // Reduce load

      if(fry.getLoad() == 0) semaphore.release(); 
      else fry.semFerryLoad.release();
  
      // Terminate
      if(isInterrupted()) break;
    }
    System.out.println("Auto "+id_auto+" terminated");
  }
}

class Ambulance extends Thread { // the Class for the Ambulance thread

  private int id;
  private int port;
  private Ferry fry;
  
  public Ambulance(int id, int prt, Ferry ferry)
  {
    this.port = prt;
    this.fry = ferry;
    this.id = id;
  }

  public void run() {
    Semaphore semaphore;
    while (true) {
      // Attente
      try {sleep((int) (1000*Math.random()));} catch (Exception e) { break;}
      System.out.println("Ambulance " + id + " arrives at port " + port);

      // Set the semaphore
      if(port == Lab4.PORT0) semaphore = fry.semPort[0];
      else semaphore = fry.semPort[1];
  
      // Board
      try{semaphore.acquire();} 
      catch (InterruptedException e) { break; }
      System.out.println("Ambulance " + id + " boards the ferry at port " + port);
      
      //***********TEST
      fry.loadAmbulance();  // increment the load  
      fry.semDeparture.release();


      // Arrive at the next port
      port = 1 - port ;   
      // Set the semaphore
      if(port == Lab4.PORT0) semaphore = fry.semPort[0];
      else semaphore = fry.semPort[1];

      //Disembarkment    
      try{fry.semFerryLoad.acquire();} catch (InterruptedException e) { break; }
      System.out.println("Ambulance " + id + " disembarks the ferry at port " + port);
      fry.unloadAmbulance();   // Reduce load
      
      if(fry.getLoad() == 0) semaphore.release();
      else fry.semFerryLoad.release(); 

      // Terminate
      if(isInterrupted()) break;
    }
    System.out.println("Ambulance " + id + " terminated.");
  }
}

class Ferry extends Thread // The ferry Class
{
  final static int MAXLOAD = 5;
  private int port=0;  // Start at port 0
  private int load=0;  // Load is zero
  private int numCrossings;  // number of crossings to execute
  private boolean ambulance_loaded = false;

  // Semaphores
  //Array of 2 semaphores for the port loading
  Semaphore[] semPort = new Semaphore[2];
  Semaphore semFerryLoad;
  Semaphore semDeparture;

  public Ferry(int prt, int nbtours)
  {
    this.port = prt;
    numCrossings = nbtours;
    semPort[0] = new Semaphore(0); //initialize the port semaphores here
    semPort[1] = new Semaphore(0); //initialize the port semaphores here
    semFerryLoad = new Semaphore(0); 
    semDeparture = new Semaphore(0);
  }

  public void run() {
    System.out.println("Start at port " + port + " with a load of " + load + " vehicles");

    semPort[0].release(MAXLOAD);

    // numCrossings crossings in our day
    for(int i=0 ; i < numCrossings ; i++) {
      semDeparture.acquireUninterruptibly();//Doesn't block thread this way!!! https://docs.oracle.com/javase/7/docs/api/java/util/concurrent/Semaphore.html
      // The crossing
      System.out.println("Departure from port " + port + " with a load of " + load + " vehicles");
      System.out.println("Crossing " + i + " with a load of " + load + " vehicles");
      if (ambulance_loaded) {
        if (load == 0) System.out.println("Error ferry leaving with less load!");
      } 
      else {
        if (load != MAXLOAD) System.out.println("Error ferry leaving with less load!");
      }
      port = 1 - port;
      try {sleep((int) (100*Math.random()));} catch (Exception e) { }
      // Arrive at port
      System.out.println("Arrive at port " + port + " with a load of " + load + " vehicles");
      // Disembarkment et loading

      semFerryLoad.release();
    }
  }

  // methodes to manipulate the load of the ferry
  public int getLoad() { 
    return(load); 
  }

  public int getPort() { 
    return(port); 
  }

  //Synchronized keyword adds intrinsic locks
  public synchronized void addLoad() {
    if (load >= MAXLOAD) System.out.println ("<<<<<<<<<< error loadig in a full Ferry! >>>>>>>>");
    load = load + 1; 
    System.out.println ("added load, now " + load);
  }
  // public void reduceLoad() throws InterruptedException { 
  public synchronized void reduceLoad() { 
    if (load <= 0) System.out.println ("<<<<<<<<<< error unloading an empty Ferry! >>>>>>>>");
    load = load - 1 ; 
    System.out.println ("removed load, now " + load);
  }
  public synchronized void loadAmbulance() {
    ambulance_loaded = true;
    addLoad();
  }
  public synchronized void unloadAmbulance(){
    ambulance_loaded = false;
    reduceLoad();
  }
}
