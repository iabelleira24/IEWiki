package iagoav.iewiki;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;

public class FavoritosActivity extends AppCompatActivity {

    private RecyclerView recyclerView;
    private RequestQueue queue;
    private String token;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_favoritos);

        recyclerView = findViewById(R.id.recyclerFavoritos);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));
        queue = Volley.newRequestQueue(this);

        SharedPreferences prefs = getSharedPreferences("session", MODE_PRIVATE);
        token = prefs.getString("token", null);

        if (token == null) {
            Toast.makeText(this, "Token no encontrado", Toast.LENGTH_SHORT).show();
            return;
        }

        cargarFavoritos();
    }

    @Override
    protected void onStart() {
        super.onStart();
        if (token != null) {
            cargarFavoritos();
        }
    }

    private void cargarFavoritos() {
        String url = "http://10.0.2.2:8000/favoritos/";

        JsonObjectRequest request = new JsonObjectRequest(
                Request.Method.GET,
                url,
                null,
                response -> {
                    try {
                        JSONArray favoritosArray = response.getJSONArray("favoritos");
                        List<JugadoresDTO> favoritosList = new ArrayList<>();

                        for (int i = 0; i < favoritosArray.length(); i++) {
                            JSONObject jugadorObj = favoritosArray.getJSONObject(i);
                            int id = jugadorObj.getInt("id");
                            String nombre = jugadorObj.getString("nombreJ");
                            String posicion = jugadorObj.getString("posicionJ");
                            String imagen = jugadorObj.getString("imagenJ");

                            favoritosList.add(new JugadoresDTO(id, nombre, posicion, imagen));
                        }

                        RecyclerViewAdapterJugadores adapter = new RecyclerViewAdapterJugadores(favoritosList);
                        recyclerView.setAdapter(adapter);

                    } catch (Exception e) {
                        e.printStackTrace();
                        Toast.makeText(this, "Error al procesar favoritos", Toast.LENGTH_SHORT).show();
                    }
                },
                error -> {
                    error.printStackTrace();
                    Toast.makeText(this, "Error de conexión", Toast.LENGTH_SHORT).show();
                }) {
            @Override
            public java.util.Map<String, String> getHeaders() {
                java.util.Map<String, String> headers = new java.util.HashMap<>();
                headers.put("token", token);
                return headers;
            }
        };

        queue.add(request);
    }
}
