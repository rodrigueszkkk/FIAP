package br.com.fiap.praticas.model;

public class Carro extends praticaModel{
    private int quantidadePortas;
    private String placa;
    private float motor = 1;


    public Carro(String modelo){
        super(modelo);
    }

    public int getQuantidadePortas() {
        return quantidadePortas;
    }

    public void setQuantidadePortas(int quantidadePortas) {
        this.quantidadePortas = quantidadePortas;
    }

    public String getPlaca() {
        return placa;
    }

    public void setPlaca(String placa) {
        this.placa = placa;
    }

    public float getMotor() {
        return motor;
    }

    public void setMotor(float motor) {
        this.motor = motor;
    }
}
