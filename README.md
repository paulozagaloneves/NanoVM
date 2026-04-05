# Terminal Linux no Browser (WASM + Alpine)

Este laboratorio disponibiliza um terminal Linux que roda no browser usando:

- **WebAssembly (WASM)** via emulador `v86`
- **Alpine Linux** via ISO oficial

## Como executar

1. Entre na pasta `terminal`.
2. Descarregue a ISO Alpine para a mesma pasta (evita problema de CORS):

```powershell
./download-alpine-iso.ps1
```

Este script descarrega a variante `alpine-virt`, mais estavel para emulacao no browser.

3. Inicie um servidor HTTP simples (abrir direto o ficheiro `index.html` nao funciona bem para WASM):

```bash
python server.py 8080
```

4. Abra no browser:

```text
http://localhost:8080
```

5. Clique em **Iniciar Alpine**.
6. Para configurar o teclado para portugues no Alpine, clique em **Teclado PT** (apos login, se necessario).
7. Para configurar a rede no Alpine, clique em **Testar Rede** (após o login)

## Observacoes

- O primeiro arranque pode demorar, pois a ISO do Alpine e os artefatos WASM sao descarregados.
- Quando o prompt aparecer, use `root` para login.
- O ambiente e efemero: ao recarregar a pagina, o estado e perdido.
- A fonte do terminal foi aumentada para melhor legibilidade.
- O laboratorio combina output de video e serial para manter compatibilidade durante o boot.
- A digitacao usa o layout do teclado do browser/sistema operativo (ex.: Portugues), com suporte para setas, Home/End, Delete e atalhos como Ctrl+C.
- A captura de teclado e global enquanto a VM estiver em execucao (exceto em campos de formulario), para evitar perda de foco no canvas.

## Troubleshooting

- Se aparecer erro de CORS ao carregar a ISO, use um espelho com CORS habilitado ou disponibilize uma ISO local na pasta `terminal` e ajuste o campo de URL.
- Se aparecer erro de `Range: bytes=... header not supported`, o laboratorio ja esta configurado para `async: false` no CDROM; recarregue a pagina com `Ctrl+F5` para limpar cache do JavaScript antigo.
- Se o terminal nao responder ao teclado, clique dentro da area preta do terminal para focar.
- Se ocorrer `V86Starter is not defined`, confirme se o HTML usa `https://cdn.jsdelivr.net/npm/v86/build/libv86.js` (sem versao fixa no caminho).
- Se ocorrer kernel panic em `setup_IO_APIC`, confirme que esta a usar `alpine-virt` e recarregue com `Ctrl+F5` para garantir o `acpi: false` atualizado.
- Se a porta `8080` estiver ocupada, inicie em outra porta, por exemplo `python server.py 8081`, e ajuste a URL da ISO no campo para `http://localhost:8081/alpine-virt-3.20.9-x86.iso`.
- Se o teclado nao responder, clique dentro da area do terminal para focar antes de digitar.