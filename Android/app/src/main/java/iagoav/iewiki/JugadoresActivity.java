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

public class JugadoresActivity extends AppCompatActivity {

    private RecyclerView recyclerView2;
    private RequestQueue queue2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_jugadores);


        findViewById(R.id.btnMisJugadores).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(JugadoresActivity.this, FavoritosActivity.class);
                startActivity(intent);
            }
        });

        recyclerView2 = findViewById(R.id.RecyclerJ);
        recyclerView2.setLayoutManager(new LinearLayoutManager(this));
        queue2 = Volley.newRequestQueue(this);

        String nombreE = getIntent().getStringExtra("name");
        Toast.makeText(this, "Cargando jugadores de: " + nombreE, Toast.LENGTH_SHORT).show();

        int equipoId = getIntent().getIntExtra("id", -1);
        if (equipoId == -1) {
            Toast.makeText(this, "ID de equipo no válido", Toast.LENGTH_SHORT).show();
            return;
        }

        String url = "http://10.0.2.2:8000/equipo/" + equipoId + "/jugadores";

        JsonObjectRequest request = new JsonObjectRequest(
                Request.Method.GET,
                url,
                null,
                response -> {
                    try {
                        JSONArray jugadoresArray = response.getJSONArray("jugadores");
                        List<JugadoresDTO> jugadoresList = new ArrayList<>();

                        for (int i = 0; i < jugadoresArray.length(); i++) {
                            JSONObject jugadorObj = jugadoresArray.getJSONObject(i);

                            int id = jugadorObj.getInt("id");
                            String nombreJ = jugadorObj.getString("nombreJ");
                            String posicionJ = jugadorObj.getString("posicionJ");
                            String imagenJ = jugadorObj.getString("imagenJ");

                            jugadoresList.add(new JugadoresDTO(id, nombreJ, posicionJ, imagenJ));
                        }

                        RecyclerViewAdapterJugadores adapter = new RecyclerViewAdapterJugadores(jugadoresList);
                        recyclerView2.setAdapter(adapter);

                    } catch (Exception e) {
                        e.printStackTrace();
                        Toast.makeText(this, "Error procesando jugadores", Toast.LENGTH_SHORT).show();
                    }
                },
                error -> {
                    error.printStackTrace();
                    Toast.makeText(this, "Error de conexión con el servidor", Toast.LENGTH_SHORT).show();
                });

        queue2.add(request);
    }
}
