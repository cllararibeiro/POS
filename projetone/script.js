// scripts.js
const apiUrl = "http://localhost:8000/tarefas/";

$(document).ready(function () {
  listarTarefas();

  $("#btnSalvar").click(function () {
    const titulo = $("#titulo").val().trim();
    const descricao = $("#descricao").val().trim();
    const concluido = $("#concluido").is(":checked");

    if (!titulo || !descricao) {
      alert("Preencha todos os campos!");
      return;
    }

    const novaTarefa = {
      id: 0,    
      titulo: titulo,
      descricao: descricao,
      concluido: concluido
    };
    const dados = JSON.stringify(novaTarefa)
    $.ajax({
      url: apiUrl,
      type: "POST",
      contentType: "application/json",
      data: dados,
      success: function (tarefa) {
        adicionarTarefaNaTabela(tarefa);
        fecharModal();
      },
      error: function () {
        alert("Erro ao cadastrar tarefa.");
      }
    });
  });
});

function listarTarefas() {
  $.get(apiUrl, function (dados) {
    dados.forEach(tarefa => {
      adicionarTarefaNaTabela(tarefa);
    });
  });
}

function adicionarTarefaNaTabela(tarefa) {
  const linha = `
    <tr data-id="${tarefa.id}">
      <td>${tarefa.id}</td>
      <td>${tarefa.titulo}</td>
      <td>${tarefa.descricao}</td>
      <td>${tarefa.concluido ? "Sim" : "Não"}</td>
      <td><button onclick="excluirTarefa(${tarefa.id}, this)">Excluir</button></td>
    </tr>
  `;
  $("#tabelaTarefas tbody").append(linha);
}

function excluirTarefa(id, botao) {
  $.ajax({
    url: apiUrl + id,
    type: "DELETE",
    success: function () {
      $(botao).closest("tr").remove();
    },
    error: function () {
      alert("Erro ao excluir tarefa.");
    }
  });
}

function abrirModal() {
  $("#modalCadastro").show();
}

function fecharModal() {
  $("#modalCadastro").hide();
  $("#titulo").val("");
  $("#descricao").val("");
  $("#concluido").prop("checked", false);
}

$(window).click(function (event) {
  if (event.target.id === "modalCadastro") {
    fecharModal();
  }
});
