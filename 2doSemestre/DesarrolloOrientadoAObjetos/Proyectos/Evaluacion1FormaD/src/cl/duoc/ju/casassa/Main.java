package cl.duoc.ju.casassa;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int opcion;

        Cliente cliente = null;
        Artista artista = null;
        Cuadro cuadro = null;
        Pedido pedido = null;

        do {
            System.out.println("===== SISTEMA DE PEDIDOS DE CUADROS ARTÍSTICOS =====");
            System.out.println("1. Ingresar Cliente");
            System.out.println("2. Ingresar Artista");
            System.out.println("3. Ingresar Cuadro");
            System.out.println("4. Generar Pedido");
            System.out.println("5. Salir");
            System.out.print("Elige una opción: ");

            opcion = sc.nextInt();
            sc.nextLine(); // limpiar buffer

            switch (opcion) {
                case 1:
                    System.out.println("--- INGRESAR CLIENTE ---");
                    System.out.print("Ingrese RUT: ");
                    String rut = sc.nextLine();
                    System.out.print("Ingrese nombre: ");
                    String nombre = sc.nextLine();
                    System.out.print("Ingrese edad: ");
                    int edad = sc.nextInt();
                    sc.nextLine();
                    cliente = new Cliente(rut, nombre, edad);
                    System.out.println("Cliente registrado con éxito.");
                    break;

                case 2:
                    System.out.println("--- INGRESAR ARTISTA ---");
                    System.out.print("Ingrese RUT: ");
                    String rutArt = sc.nextLine();
                    System.out.print("Ingrese nombre: ");
                    String nombreArt = sc.nextLine();
                    System.out.print("Ingrese nro_artista: ");
                    int nroArt = sc.nextInt();
                    sc.nextLine();
                    System.out.print("Ingrese fecha de ingreso: ");
                    String fecha = sc.nextLine();
                    System.out.print("Ingrese galería: ");
                    String galeria = sc.nextLine();
                    artista = new Artista(nombreArt, rutArt, nroArt, fecha, galeria);
                    System.out.println("Artista registrado con éxito.");
                    break;

                case 3:
                    System.out.println("--- INGRESAR CUADRO ---");
                    System.out.print("Ingrese código: ");
                    int codigo = sc.nextInt();
                    sc.nextLine();
                    System.out.print("Ingrese nombre del cuadro: ");
                    String nombreCuadro = sc.nextLine();
                    System.out.print("Ingrese tipo de técnica (Óleo, Acrílico, Carbón): ");
                    String tecnica = sc.nextLine();
                    System.out.print("Ingrese tipo de arte (Moderno, Clásico, Contemporáneo): ");
                    String tipoArte = sc.nextLine();
                    cuadro = new Cuadro(codigo, nombreCuadro, tecnica, tipoArte);
                    System.out.println("Cuadro registrado con éxito.");
                    break;

                case 4:
                    System.out.println("--- GENERAR PEDIDO ---");
                    if (cliente == null || artista == null || cuadro == null) {
                        System.out.println("Debe ingresar primero cliente, artista y cuadro.");
                    } else {
                        System.out.print("Ingrese cantidad: ");
                        int cantidad = sc.nextInt();
                        sc.nextLine();
                        pedido = new Pedido(cliente, artista, cuadro, cantidad, "01/01/2025");
                        System.out.println("Pedido generado.");
                        System.out.println("Total bruto: $" + pedido.calcularTotalBruto());
                        System.out.println("Descuento: $" + pedido.calcularDescuento());
                        System.out.println("Total neto: $" + pedido.calcularTotalNeto());
                    }
                    break;

                case 5:
                    System.out.println("Saliendo del sistema...");
                    break;

                default:
                    System.out.println("Opción inválida, intente nuevamente.");
            }

            System.out.println();

        } while (opcion != 5);

        sc.close();
    }
