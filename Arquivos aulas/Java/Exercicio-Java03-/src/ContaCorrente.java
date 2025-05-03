public class ContaCorrente {
    double saldo;
    Cliente titular;

    void depositar(double valor){

        saldo = saldo + valor;
    }

    void retirar(double valor){

        saldo = saldo - valor;
    }

    double retornarSaldo(){
        return saldo;
    }
}
