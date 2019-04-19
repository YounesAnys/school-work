/**
 * Main class where the execution will start from
 * @author Hussein Al Osman
 */
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {



	/**
	 * Get all the files from a directory
	 * @param dir File instance representing the directory
	 * @return Array List of all the files in the directory
	 */
	private static ArrayList<File> getFiles (File dir){
		ArrayList<File> filesList = new ArrayList<File>();

		String [] fileNames = dir.list();

		for (String fileName: fileNames){
			File file = new File(dir.getAbsoluteFile()+"/"+fileName);
			if (file.isFile()){
				filesList.add(file);
			}

		}

		return filesList;
	}


	public static void main(String args[]) throws IOException {

		if (args.length > 0){ // Make sure an argument was passed to this program

			// The argument should represent a directory
			File dir = new File (args[0]);

			// Check if dir is in fact a directory
			if (dir.isDirectory()){

				// Read the files in the directory
				ArrayList<File> filesList = getFiles(dir);

				System.out.println("Enter the pattern to look for:");
				Scanner scanIn = new Scanner(System.in);
				String line  = scanIn.nextLine();
				scanIn.close();

				// Create an array of search jobs
				SearchJob [] jobs = new SearchJob[filesList.size()];
				for (int i = 0; i < jobs.length; i++){
					jobs[i] = new SearchJob(filesList.get(i));
				}


				long t1 = System.currentTimeMillis();
				ThreadGroup threadGroup = new ThreadGroup("Search Tasks");
				int threadGroupSize = 4;
				int lengthSize = (int)Math.ceil((double)jobs.length/(double)threadGroupSize);
				SearchTask [] searchTask = new SearchTask [threadGroupSize];

        for (int i = 0; i < lengthSize; i++){
          for (int j = 0; j < threadGroupSize; j++){
						int jobIndex = i*threadGroupSize + j;
            if (jobIndex < jobs.length){ // make sure you do no exceed the number of available jobs
              if (searchTask[j] == null){
								searchTask[j] = new SearchTask(jobs[i*threadGroupSize + j], line);
							}
							else {
								searchTask[j].setJob(jobs[i*threadGroupSize + j]);
							}
              new Thread(threadGroup, searchTask[j]).start();
						}
					}
					while (threadGroup.activeCount() > 0);
				}


				long t2 = System.currentTimeMillis();

				long resultTime = t2 - t1;

				System.out.println("Execution Time: "+resultTime+" ms");
			}
			else {
				// The argument specified is not a path for a directory
				System.err.println("Incorrect argument: must be a directory");
			}
		}
		else {
			// No argument were passed to the program
			System.err.println("Missing argument: files directory");
		}
    }

}
