public class Aluno {
    String nome;
    double cp1;
    double cp2;
    double challenge;
    double gs;

    double calcularMediaCp(){
        double mediaCP = (cp1 + cp2) / 2;
        return mediaCP;
    }
    double calcularMediaSemestral(){
        double mediaCP = calcularMediaCp();
        double media = mediaCP * 0.2 + challenge * 0.2 + gs * 0.6;
        return media;
    }
}