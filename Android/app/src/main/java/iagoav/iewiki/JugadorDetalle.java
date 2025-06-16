package iagoav.iewiki;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.android.volley.Request;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;
import com.squareup.picasso.Picasso;

import org.json.JSONObject;

public class JugadorDetalle extends AppCompatActivity {

    private TextView textViewNombre;
    private TextView textViewPosicion;
    private TextView textViewSupertecnica;
    private TextView textViewEquipo;
    private ImageView imageViewJugador;
    private ImageButton botonCorazon;
    private boolean esFavorito = false;
    private int jugadorId;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detallejugador);

        textViewNombre = findViewById(R.id.nombreJ);
        textViewPosicion = findViewById(R.id.posicionJ);
        textViewSupertecnica = findViewById(R.id.supertecnicaJ);
        textViewEquipo = findViewById(R.id.nombreE);
        imageViewJugador = findViewById(R.id.imagenJ);
        botonCorazon = findViewById(R.id.botonCorazon);

        botonCorazon.setVisibility(View.VISIBLE);
        botonCorazon.bringToFront();

        jugadorId = getIntent().getIntExtra("id", -1);
        if (jugadorId == -1) {
            Toast.makeText(this, "ID de jugador no válido", Toast.LENGTH_SHORT).show();
            finish();
            return;
        }

        SharedPreferences prefs = getSharedPreferences("session", MODE_PRIVATE);
        String token = prefs.getString("token", null);

        String url = "http://10.0.2.2:8000/jugadores/" + jugadorId + "/";

        JsonObjectRequest request = new JsonObjectRequest(
                Request.Method.GET,
                url,
                null,
                response -> {
                    try {
                        String nombreJ = response.getString("nombreJ");
                        String posicionJ = response.getString("posicionJ");
                        String supertecnicaJ = response.getString("supertecnicaJ");
                        String equipoJ = response.getString("equipoJ");
                        String imagenJ = response.getString("imagenJ");

                        textViewNombre.setText(nombreJ);
                        textViewPosicion.setText(posicionJ);
                        textViewSupertecnica.setText(supertecnicaJ);
                        textViewEquipo.setText(equipoJ);

                        String imageUrl = "http://10.0.2.2:8000" + imagenJ;
                        Picasso.get().load(imageUrl).into(imageViewJugador);


                        esFavorito = response.optBoolean("favorito", false);
                        if (esFavorito) {
                            botonCorazon.setImageResource(R.drawable.lleno);
                        } else {
                            botonCorazon.setImageResource(R.drawable.vacio);
                        }

                    } catch (Exception e) {
                        e.printStackTrace();
                        Toast.makeText(this, "Error procesando datos del jugador", Toast.LENGTH_SHORT).show();
                    }
                },
                error -> {
                    error.printStackTrace();
                    Toast.makeText(this, "Error de conexión con el servidor", Toast.LENGTH_SHORT).show();
                }
        ) {
            @Override
            public java.util.Map<String, String> getHeaders() {
                java.util.Map<String, String> headers = new java.util.HashMap<>();
                if (token != null) {
                    headers.put("token", token);
                }
                return headers;
            }
        };

        Volley.newRequestQueue(this).add(request);

        botonCorazon.setOnClickListener(v -> {
            if (token == null) {
                Toast.makeText(this, "Token no disponible", Toast.LENGTH_SHORT).show();
                return;
            }

            JSONObject json = new JSONObject();
            try {
                json.put("jugadorId", jugadorId);
            } catch (Exception e) {
                e.printStackTrace();
                return;
            }

            JsonObjectRequest likeRequest = new JsonObjectRequest(
                    Request.Method.PUT,
                    "http://10.0.2.2:8000/like/",
                    json,
                    response -> {
                        try {
                            esFavorito = response.getBoolean("favorito");

                            if (esFavorito) {
                                botonCorazon.setImageResource(R.drawable.lleno);
                                Toast.makeText(this, "Añadido a favoritos", Toast.LENGTH_SHORT).show();
                            } else {
                                botonCorazon.setImageResource(R.drawable.vacio);
                                Toast.makeText(this, "Eliminado de favoritos", Toast.LENGTH_SHORT).show();
                            }
                        } catch (Exception e) {
                            e.printStackTrace();
                        }
                    },
                    error -> {
                        error.printStackTrace();
                        Toast.makeText(this, "Error al marcar favorito", Toast.LENGTH_SHORT).show();
                    }
            ) {
                @Override
                public java.util.Map<String, String> getHeaders() {
                    java.util.Map<String, String> headers = new java.util.HashMap<>();
                    headers.put("token", token);
                    return headers;
                }
            };

            Volley.newRequestQueue(this).add(likeRequest);
        });
    }
}
