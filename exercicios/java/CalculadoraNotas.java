import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class CalculadoraNotas {

    private static final double PASS_MARK = 60.0;
    private static final Scanner SCANNER = new Scanner(System.in);
    private static final Random RANDOM = new Random();

    public static void main(String[] args) {
        while (true) {
            String opcao = menu();

            switch (opcao) {
                case "1" -> {
                    double media = calculaMediaVirtual();
                    mostraStatus(media);
                }
                case "2" -> {
                    double media = calculaMediaVirtual();
                    mostraStatus(media);
                    double mediaMaligna = modoMaligno(media);
                    mostraStatus(mediaMaligna);
                }
                case "3" -> {
                    System.out.println("Saindo... que a maldade deixe apenas o suspense.");
                    return;
                }
                default -> System.out.println("Opção inválida. Tente novamente.");
            }
        }
    }

    private static String menu() {
        System.out.println("\n=== CALCULADORA DE NOTA MALIGNA ===");
        System.out.println("1 - Calcular média escolar");
        System.out.println("2 - Calcular média e acionar modo maligno");
        System.out.println("3 - Sair");
        System.out.print("Escolha uma opção: ");
        return SCANNER.nextLine().trim();
    }

    private static double leiaDouble(String prompt, double minimo, double maximo) {
        while (true) {
            System.out.print(prompt);
            String linha = SCANNER.nextLine().trim().replace(',', '.');
            try {
                double valor = Double.parseDouble(linha);
                if (valor >= minimo && valor <= maximo) {
                    return valor;
                }
                System.out.printf("Digite um valor entre %.1f e %.1f.%n", minimo, maximo);
            } catch (NumberFormatException ex) {
                System.out.println("Entrada inválida. Use apenas números.");
            }
        }
    }

    private static double calculaMediaPonderada(List<NotaPeso> avaliacoes) {
        double somaPesos = 0.0;
        double somaNotas = 0.0;
        for (NotaPeso aval : avaliacoes) {
            somaPesos += aval.peso();
            somaNotas += aval.nota() * aval.peso();
        }
        if (somaPesos == 0.0) {
            return 0.0;
        }
        return somaNotas / somaPesos;
    }

    private static double modoMaligno(double mediaAtual) {
        System.out.println("\nModo Maligno ativado! A noite está escura e as notas tremem...");
        if (mediaAtual >= PASS_MARK) {
            System.out.println("Você já escapou da reprovação, mas o mal não descansa.");
            double melhora = Math.min(100.0 - mediaAtual, 1.0 + RANDOM.nextDouble() * 4.0);
            double novaMedia = mediaAtual + melhora;
            System.out.printf("Curva sombria adicionou +%.1f pontos à média. Nova média: %.1f%n", melhora, novaMedia);
            return novaMedia;
        }

        double deficit = PASS_MARK - mediaAtual;
        System.out.printf("Sua média atual é %.1f. O abismo da reprovação está a %.1f pontos.%n", mediaAtual, deficit);
        System.out.println("O mal oferece um pacto: um salto sombrio de esperança... Mas cuidado, ele custa suspense e nervos.");

        double bonusMin = Math.max(0.0, deficit * 0.7);
        double bonusMax = Math.min(100.0 - mediaAtual, deficit * 1.3);
        double bonus = bonusMin + RANDOM.nextDouble() * Math.max(0.0, bonusMax - bonusMin);
        double novaMedia = Math.min(100.0, mediaAtual + bonus);

        if (novaMedia >= PASS_MARK) {
            System.out.printf("A curva maligna funciona! Nova média: %.1f. Você escapou da reprovação... por agora.%n", novaMedia);
        } else {
            System.out.printf("A maldade falhou um pouco. Nova média: %.1f. Ainda precisa de %.1f pontos.%n", novaMedia, PASS_MARK - novaMedia);
        }
        return novaMedia;
    }

    private static double calculaMediaVirtual() {
        System.out.println("\nVamos montar sua nota maligna. Quantas avaliações você quer usar?");
        int quantidade = (int) leiaDouble("Digite o número de avaliações (2-10): ", 2.0, 10.0);
        List<NotaPeso> avaliacoes = new ArrayList<>();

        for (int i = 1; i <= quantidade; i++) {
            double nota = leiaDouble("Nota da avaliação " + i + " (0-100): ", 0.0, 100.0);
            double peso = leiaDouble("Peso da avaliação " + i + " (1-10): ", 1.0, 10.0);
            avaliacoes.add(new NotaPeso(nota, peso));
        }

        double media = calculaMediaPonderada(avaliacoes);
        System.out.printf("\nSua média ponderada é: %.1f%n", media);
        return media;
    }

    private static void mostraStatus(double media) {
        if (media >= PASS_MARK) {
            System.out.println("Status: APROVADO! Que seja um triunfo maligno...");
        } else {
            System.out.println("Status: REPROVADO. O terror das notas continua presente.");
        }
    }

    private record NotaPeso(double nota, double peso) {
    }
}
