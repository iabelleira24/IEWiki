package iagoav.iewiki;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Toast;
import android.view.View;

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

public class CatalogoJugadoresActivity extends AppCompatActivity {
    private RecyclerView recyclerView3;
    private RequestQueue queue3;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_catalogo);

        recyclerView3 = findViewById(R.id.RecyclerC);
        recyclerView3.setLayoutManager(new LinearLayoutManager(this));
        queue3 = Volley.newRequestQueue(this);


        Toast.makeText(this, "Cargando todos los jugadores ", Toast.LENGTH_SHORT).show();


        String url = "http://10.0.2.2:8000/jugadores/";

        JsonObjectRequest request = new JsonObjectRequest(
                Request.Method.GET,
                url,
                null,
                response -> {
                    try {
                        JSONArray jugadoresArray2 = response.getJSONArray("jugadores");
                        List<JugadoresCatalogoDTO> jugadoresList2 = new ArrayList<>();

                        for (int c = 0; c < jugadoresArray2.length(); c++) {
                            JSONObject jugadorObj2 = jugadoresArray2.getJSONObject(c);

                            int id = jugadorObj2.getInt("id");
                            String nombreJ = jugadorObj2.getString("nombreJ");

                            String imagenJ = jugadorObj2.getString("imagenJ");

                            jugadoresList2.add(new JugadoresCatalogoDTO(id, nombreJ, imagenJ));
                        }
                        RecyclerViewAdapterCatalogo adapter2 = new RecyclerViewAdapterCatalogo(jugadoresList2);
                        recyclerView3.setAdapter(adapter2);
                    } catch (Exception e) {
                        e.printStackTrace();
                        Toast.makeText(this, "Error procesando jugadores", Toast.LENGTH_SHORT).show();
                    }
                },
                error -> {
                    error.printStackTrace();
                    Toast.makeText(this, "Error de conexión con el servidor", Toast.LENGTH_SHORT).show();
                });

        queue3.add(request);

    }

}