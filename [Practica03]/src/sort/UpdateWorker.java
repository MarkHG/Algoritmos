package sort;

import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.io.File;
import java.util.List;
import javax.imageio.ImageIO;
import javax.swing.ImageIcon;
import javax.swing.JLabel;
import javax.swing.SwingWorker;

public class UpdateWorker extends SwingWorker<BufferedImage, BufferedImage>{

  private BufferedImage referencia;
  private JLabel target;
  private BufferedImage copia;
  private int[] arreglo;
  private int framerate;
  private int n;
  private String metodo;
  private int iteracion;
  private int arreglo2;
  private int izq;
  private int m;
  private int der;


  public UpdateWorker(int[] numeros, JLabel target, String archivo, BufferedImage master, int speed, String algoritmo){
    this.arreglo = numeros;
    this.target = target;
    try{
      referencia = ImageIO.read(new File("resource/"+archivo));
      copia = master;
      n = copia.getHeight()*copia.getWidth();
    }catch(Exception e){
      System.err.println(":c Esto no deberia ocurrir");
    }
    framerate = speed; // Indica cada cuantas iteraciones se actualizara la imagen
    metodo = algoritmo;
    iteracion = 0;
  }

  public BufferedImage updateImage(){
    Graphics2D g = copia.createGraphics();
    g.drawImage(copia, 0, 0, null);
    g.dispose();
    return copia;
  }

  @Override
  protected void process(List<BufferedImage> chunks){
    target.setIcon(new ImageIcon(chunks.get(chunks.size() - 1)));
  }

  public void update(){
    for(int i = 0; i < n; i++){
      int indiceDeOriginal = arreglo[i];
      int colOriginal = indiceDeOriginal%copia.getWidth();
      int renOriginal = indiceDeOriginal/copia.getWidth();
      int colI = i%copia.getWidth();
      int renI = i/copia.getWidth();
      copia.setRGB(colI, renI, referencia.getRGB(colOriginal, renOriginal));
    }
    publish(updateImage());
  }

  @Override
  protected BufferedImage doInBackground() throws Exception{
    if(metodo.equals("bubble"))
    bubbleSort();
    if(metodo.equals("exchange"))
    exchangeSort();
    if(metodo.equals("insertion"))
    insertionSort();
    if(metodo.equals("selection"))
    selectionSort();
    if(metodo.equals("merge"))
    mergeSort();
    update();
    return null;
  }

  private void bubbleSort(){
    for(int i = 0; i < n-1; i++){
      for(int j = 0; j < n-i-1; j++){
        if(arreglo[j] > arreglo[j+1])
        swap(j, j+1);
      }
      if(iteracion%framerate == 0) update(); // Actualizamos la interfaz grafica solo si han pasado el numero de iteraciones deseadas
      iteracion = (iteracion+1)%framerate; // Aumentamos el numero de iteraciones
    }
  }

  private void exchangeSort(){
    for ( int i = 0; i < arreglo.length-1; i ++ ){
         for (int j = i + 1; j < arreglo.length; j ++ ){
              if( arreglo[ i ] < arreglo[ j ] ) {
              swap(i, j);

               }

             }
             if(iteracion%framerate == 0) update(); // Actualizamos la interfaz grafica solo si han pasado el numero de iteraciones deseadas
             iteracion = (iteracion+1)%framerate; // Aumentamos el numero de iteraciones
           }
         }

  private void insertionSort(){
    int  nuevoValor;
    for (int i = 1; i < arreglo.length; i++){
      nuevoValor = arreglo[i];
      int j;
      j = i;
      while (j > 0 && arreglo [j - 1] > nuevoValor) {
        arreglo[j] = arreglo[j - 1];
        j--;
      }
      arreglo[j] = nuevoValor;
    }
    if(iteracion%framerate == 0) update(); // Actualizamos la interfaz grafica solo si han pasado el numero de iteraciones deseadas
    iteracion = (iteracion+1)%framerate; // Aumentamos el numero de iteraciones
  }

  private void selectionSort(){
    for (int i=0; i < arreglo.length-1; i++) {
      for (int j=i+1; j < arreglo.length; j++) {
          if (arreglo[i] > arreglo[j]) {
          swap(i, j);

         }
      }
      if(iteracion%framerate == 0) update(); // Actualizamos la interfaz grafica solo si han pasado el numero de iteraciones deseadas
      iteracion = (iteracion+1)%framerate; // Aumentamos el numero de iteraciones
    }
  }

  private void mergeSort(){
    /** if (izq<der){
    int m=(izq+der)/2;
    mergeSort(arreglo,izq, m);
    mergeSort(arreglo,m+1, der);
    int i, j, k;
    int[]arreglo2 = new int[arreglo.length];
    for (i= izq; i <= der; i++)
      arreglo2[i] = arreglo[i];
      i=izq; j=m+1; k=izq;
      while (i <= m && j <= der)
      if (arreglo2[i] <= arreglo2[j])
        arreglo[k++] = arreglo[i++];
      else
        arreglo[k++] = arreglo[j++];
      while (i <= m)
        arreglo[k++] = arreglo[i++];;
    } */
  }

  public void swap(int i, int j){
    int aux = arreglo[i];
    arreglo[i] = arreglo[j];
    arreglo[j] = aux;
  }

}
