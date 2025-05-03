package br.com.fiap.hospital.model;

public class Medico {
    private String nome;
    private int crm;
    private String especialidades;
    private boolean ativo;

    //Construtores = pode criar diversos, quantos necessários
    public Medico(String nome, int crm, String especialidades, boolean ativo){
        this.nome = nome;
        this.crm = crm;
        this.especialidades = especialidades;
        this.ativo = ativo;
    }
//getters and setters
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getCrm() {
        return crm;
    }

    public void setCrm(int crm) {
        this.crm = crm;
    }

    public String getEspecialidades() {
        return especialidades;
    }

    public void setEspecialidades(String especialidades) {
        this.especialidades = especialidades;
    }

    public boolean isAtivo() {
        return ativo;
    }

    public void setAtivo(boolean ativo) {
        this.ativo = ativo;
    }
}
