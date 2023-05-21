//Generador de contraseñas aleatorias de 45 caracteres de longitud

import java.io.*;

public class Claves{

    //en args 0 se guarda el nonbre del archivo .txt donde se guardan las claves
    //en args 1 se guarda la longitud de la clave

    public static void main(String[] args){

      int longitudArgs = args.length;

      if (longitudArgs == 0) {

        System.out.println("Error --> añade argumentos \n\n"
                            + "\targs[0] = nombre fichero\n"
                            +"\targs[1] = longitud clave\n"
                            +"\targs[2,...,n] = inicial app para la clave.");
        return;

      }

      PrintWriter salida = null;
      String clave = "";
      String caracteres = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()1234567890 .,;:";
      int numeroAleatorio;
      final int longitudClave = Integer.parseInt(args[1]);
      final int valorMin = 1;
      final int valorMax = caracteres.length() + 1;

      try {

          salida = new PrintWriter(new FileOutputStream(args[0]+".txt"));

      } catch (Exception ex) {

          System.out.println("Error");
          System.exit(-1);

      }

      //bucle Generador
      for (int j = 2; j <= (longitudArgs - 1); j++){

        for(int i = 1; i <= longitudClave; i++){

          numeroAleatorio = (int) (Math.random()*(valorMax - valorMin));
          clave = clave + caracteres.charAt(numeroAleatorio);

        }

        salida.println(clave + " --> " + args[j]);
        salida.println("-------------------------------------");
        clave = "";

      }

      salida.close();

    }

}
