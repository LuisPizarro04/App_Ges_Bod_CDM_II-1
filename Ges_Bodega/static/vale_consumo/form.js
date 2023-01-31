var tblProducts;
var vents = {
    items: {
        solicitante: '',
        fecha_solicitud: '',
        recursos: []
    },
    add: function(item){
        this.items.recursos.push(item);
        this.list();
    },
    list: function () {
        tblProducts = $('#tblProducts').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            data: this.items.recursos,
            columns: [
                {"data": "id"},
                {"data": "nombre_recurso"},
                {"data": "cantidad_solicitada"},

            ],
            rowCallback(row, data, displayNum, displayIndex, dataIndex) {

                $(row).find('input[name="cantidad_solicitada"]').TouchSpin({
                    min: 1,
                    max: 1000000000,
                    step: 1
                });

            },
            columnDefs: [
                {
                    targets: [0],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<a rel="remove" class="btn btn-danger rounded-pill">Danger</a>';
                        //return '<a rel="remove" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                        
                    }
                },
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cantidad_solicitada" class="form-control form-control-sm" autocomplete="off" value="'+row.cantidad_solicitada+'">';
                    }
                },
            ],
            
            initComplete: function (settings, json) {

            }
        });
    },
};

$(function () {
    // search products

    $('input[name="search"]').autocomplete({
        source: function (request, response) {
            $.ajax({
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'search_products',
                    'term': request.term
                },
                dataType: 'json',
            }).done(function (data) {
                response(data);
            }).fail(function (jqXHR, textStatus, errorThrown) {
                //alert(textStatus + ': ' + errorThrown);
            }).always(function (data) {

            });
        },
        delay: 500,
        minLength: 1,
        select: function (event, ui) {
            event.preventDefault();
            console.clear();
            ui.item.cantidad_solicitada = 1;            
            console.log(vents.items);
            vents.items.recursos.push(ui.item);
            vents.list();
            $(this).val('');
        }
    });
    // aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    // event cant

    $('#tblProducts tbody')
        .on('click', 'a[rel="remove"]', function () {
            var tr = tblProducts.cell($(this).closest('td, li')).index();
            //alert_action('Notificación', '¿Estas seguro de eliminar el producto de tu detalle?', function () {
            vents.items.recursos.splice(tr.row, 1);
            vents.list();
            //});
        });
    // event submit
    $('form').on('submit', function (e) {
        e.preventDefault();
        vents.items.solicitante = $('input[name="solicitante"]').val();
        vents.items.fecha_solicitud = $('input[name="fecha_solicitud"]').val();
        var parameters = new FormData()
        parameters.append('action', $('input[name="action"]').val());
        parameters.append('vents', JSON.stringify(vents.items));        
    });
});